import numpy as np




class PoissonEventGenerator(object):
    def __init__(self, function):
        """
        :param function: a function of time from which to generate events

        """

        self._function = function

    def non_homogeneous_poisson_generator(self, tstart, tstop, *params):
        """
        Non-homogeneous poisson process generator
        for a given max rate and time range, this function
        generates time tags sampled from the energy integrated
        lightcurve.


        """

        num_time_steps = 1000

        time_grid = np.linspace(tstart, tstop + 1., num_time_steps)
        tmp = self._function(time_grid,*params)

        fmax = tmp.max()

        time = tstart

        arrival_times = [tstart]

        while time < tstop:

            time = time - (1. / fmax) * np.log(np.random.rand())
            test = np.random.rand()

            p_test = self._function(time) / fmax

            if test <= p_test:
                arrival_times.append(time)

        return np.array(arrival_times)
