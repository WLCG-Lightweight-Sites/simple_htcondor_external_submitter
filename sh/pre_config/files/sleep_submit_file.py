from config_file import ConfigFile


class SleepSubmitFile(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_advanced_parameters(self):
        super().add_advanced_parameters()
        condor_host = self.lightweight_component['config']['condor_host']
        condor_host_port = self.lightweight_component['config']['condor_host_port']
        self.advanced_category.add(
            """universe                = grid
executable              = sleep.sh
log                     = sleep.log
output                  = outfile.txt
error                   = errors.txt
should_transfer_files   = Yes
when_to_transfer_output = ON_EXIT
use_x509userproxy = true
+WantJobRouter = true
+TransferOutput = ""
grid_resource = condor {grid_resource} {grid_resource}:{grid_resource_port}
queue""".format(grid_resource=condor_host, grid_resource_port=condor_host_port))
