'''
This module contains the InterpolatorClass, which performs interpolation in the boosted fireball Table.

'''

import numpy as np
import h5py as h5

class InterpolatorClass:
    '''
    InterpolatorClass performs interpolation in the boosted fireball Table. 
    '''
    ### Private: h5 Table
    _Table = {}
    _Axis = {}
    
    ### Private: interpolation function
    _f_peak = None
    _f_nu_c = None
    _f_nu_m = None

    
    
    def __init__(self, Table, LogTable=True, LogAxis=['tau']):
        '''
        Initialize InterpolatorClass.
        
        Args:
            Table (str): directory to boosted fireball table
            LogTable (bool): whether Table is measured in log scale
            LogAxis (list of str): whether certain axis is measured in log scale
        '''
        self._LoadTable(Table)
        self._SetScale(LogTable=True,LogAxis=['tau'])
        self._GetInterpolator()
    
    ### Private Function
    def _LoadTable(self, Table):
        '''
        Load boosted fireball Table.

        Args:
            Table (str): directory to boosted fireball table
        '''
        Data = h5.File(Table, 'r')
        for key in Data.keys():
            if key in ['f_peak','f_nu_c','f_nu_m']:
                self._Table[key] = Data[key][...]
            else:
                self._Axis[key] = Data[key][...]
       
        #print('whats been loaded into the table', self._Table['f_nu_m']) #All good, some zeros but no -inf, same for fnuc and fnum
        #print('whats in the axis', self._Axis, 'in np.log', np.log(self._Axis['tau']))

        ### Due to some reasons, we need to convert bytes to string. 
        self._Axis['Axis'] = np.array([x.decode("utf-8") for x in self._Axis['Axis']])
        Data.close()
    
    
    def _SetScale(self, LogTable=True,LogAxis=['tau']):
        '''
        Set proper scales to table and axis.

        Args:
            LogTable (bool): whether Table is measured in log scale
            LogAxis (list of str): whether certain axis is measured in log scale
        '''

        self.Info = self._Axis.copy()

        if 'LogAxis' not in self._Axis.keys():
            self._Axis['LogAxis'] = LogAxis
            for key in LogAxis:
                if key not in self._Axis.keys():
                    raise ValueError('could not find %s in Axis' %(key))
                else:
                    self._Axis[key] = np.log(self._Axis[key])

        #print('Axis setscale', self._Axis['tau']) # Good

        if 'LogTable' not in self._Table.keys():
            for key in self._Table.keys():
                temp = np.ma.log(self._Table[key]) #np.ma masks all the non valid input for the log function
                #print(temp.filled(np.log(small)))
                self._Table[key] = temp.filled(-np.inf) #the masked input recieves the value in the filled (used to be -inf)
                #print('key self table',self._Table[key]) #np.log(small))
            self._Table['LogTable'] = True
            
        #print('Setscale', self._Table['f_nu_m']) # Not Good: Setscale turns all the zeros into -inf
    
    
    def _GetInterpolator(self):
        '''
        Use scipy.interpolate.RegularGridInterpolator to perform interpolation.
        '''
        from scipy.interpolate import RegularGridInterpolator

        Axes = [self._Axis[key] for key in self._Axis['Axis']]

        #print('Axes',Axes[0]) #All good here they're already written in the paper
        #print('Axes shape',np.shape(Axes[3])) #The shapes match, it's all good
        self._f_peak = RegularGridInterpolator(Axes, self._Table['f_peak'],bounds_error=True, fill_value=None) 
        self._f_nu_c = RegularGridInterpolator(Axes, self._Table['f_nu_c'],bounds_error=True, fill_value=None) 
        self._f_nu_m = RegularGridInterpolator(Axes, self._Table['f_nu_m'],bounds_error=True, fill_value=None) 
        #bounds_error = False will use fill value instead of raising an error when the value is out of bounds (defulat is True)
        #Fill value = None will extrapolate the values (default is nan, but it can also be set to 0)
        #print('self table', self._Table['f_peak']) #We can see -inf in some lines
        #print('self table shape', np.shape(self._Table['f_peak'])) #The shapes match, it's all good

        
    
    ### Public Function
    def GetTableInfo(self):
        '''
        Get Table Information. 

        Return:
            dict
        '''
        return self.Info
    
    
    def GetValue(self, Position):
        '''
        Get the characteristic function values at the Position. 

        Args:
            Position (Array): (tau, Eta0, GammaB, theta_obs) (linear scale)
        Return:
            float, float, float: characteristic function values

        '''

        ScaledPosition = Position.copy()
        #print('before the conversion:', ScaledPosition)

        ### convert linear scale to log scale
        for key in self._Axis['LogAxis']:
            idx = np.where(self._Axis['Axis'] == key)[0][0]
            ScaledPosition[:,idx] = np.log(ScaledPosition[:,idx])

        #print('after the conversion:', ScaledPosition) #It converted only E so it worked

        ### When lorentz factor is low and observation time is ealry, there is no detection, which is represented by nans. 
        #test = np.shape(ScaledPosition)*1
        #print(ScaledPosition[:,0])
        #print('f_peak', self._f_peak(ScaledPosition))

        try:
            if self._Table['LogTable']:
                #print('Made it to the if')
                #print('f_peak', self._f_peak(ScaledPosition))
                f_peak = np.exp(self._f_peak(ScaledPosition))
                #print('break1')
                f_nu_c = np.exp(self._f_nu_c(ScaledPosition))
                #print('break2')
                f_nu_m = np.exp(self._f_nu_m(ScaledPosition))
                #print('sucessfully through the if')
                #print('from the try:', f_peak,f_nu_c,f_nu_m)

            else:
                #print('Made it to the else')
                #np.seterr(all='ignore') #Will ignore all warnings about mathematical errors (div by 0...)
                f_peak = self._f_peak(ScaledPosition)
                f_nu_c = self._f_nu_c(ScaledPosition)
                f_nu_m = self._f_nu_m(ScaledPosition)
                #np.seterr(all='raise')
                #print('from the try else:', f_peak,f_nu_c,f_nu_m)
            return f_peak, f_nu_c, f_nu_m
        
        #Handles the errors by overwrtiting th values as Nans
        except:
            #print('Made it to the exept')
            Nans = [np.nan for x in range(len(Position))]
            f_peak, f_nu_c, f_nu_m = Nans, Nans, Nans
            return f_peak, f_nu_c, f_nu_m
    
    
    
    
