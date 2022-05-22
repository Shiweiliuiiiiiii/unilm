import mmcv
from mmcv.runner import HOOKS, Hook


@HOOKS.register_module()
class ApplyMaskHook(Hook):
    """
    Customized masking operation.
    """

    def before_iter(self, runner):
        """
        Apply mask before each update
        """
        runner.model.apply_mssk()

    def after_iter(self, runner):
        """
        Apply mask after each update
        """
        runner.model.apply_mssk()