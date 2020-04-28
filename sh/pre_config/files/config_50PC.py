from models.config_file import ConfigFile
from generic_helpers import get_dns_info
import array


class SubmitConfig(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_static_parameters(self):
        super().add_static_parameters()
        self.static_category.add("Use Role: submit\n")
        self.static_category.add_key_value("allow_write", "*")

    def add_advanced_parameters(self):
        super().add_advanced_parameters()
        condor_host_execution_id = self.lightweight_component['config']['condor_host_execution_id']
        condor_host_dns = get_dns_info(self.augmented_site_level_config, condor_host_execution_id)
        condor_host_ip = condor_host_dns['container_ip']
        self.advanced_category.add_key_value("condor_host", condor_host_ip)
