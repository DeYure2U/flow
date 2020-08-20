"""Contains the RLController class."""

from flow.controllers.base_controller import BaseController


class RLController(BaseController):
    """RL Controller.

    Vehicles with this class specified will be stored in the list of the RL IDs
    in the Vehicles class.

    Usage: See base class for usage example.

    Attributes
    ----------
    veh_id : str
        Vehicle ID for SUMO identification

    Examples
    --------
    A set of vehicles can be instantiated as RL vehicles as follows:

        >>> from flow.core.params import VehicleParams
        >>> vehicles = VehicleParams()
        >>> vehicles.add(acceleration_controller=(RLController, {}))

    In order to collect the list of all RL vehicles in the next, run:

        >>> from flow.envs import Env
        >>> env = Env(...)
        >>> rl_ids = env.k.vehicle.get_rl_ids()
    """

    def __init__(self, veh_id, car_following_params, fail_safe=None, default_controller=None):
        """Instantiate an RL Controller."""
        BaseController.__init__(
            self,
            veh_id,
            car_following_params,
            fail_safe=fail_safe,
        )
        # This controller is used in the segments where the RL is not allowed to apply control
        if default_controller is not None:
            self.default_controller = default_controller[0](veh_id=veh_id, car_following_params=car_following_params,
                                                            **default_controller[1])

    def get_accel(self, env):
        """Pass, as this is never called; required to override abstractmethod."""
        pass

    def get_custom_accel(self, this_vel, lead_vel, h):
        """See parent class."""
        raise NotImplementedError
