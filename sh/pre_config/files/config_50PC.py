from models.config_file import ConfigFile
import array


class SubmitConfig(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_static_parameters(self):
        super().add_static_parameters()
        self.static_category.add("Use Role: submit\n")
        self.static_category.add_key_value("allow_write", "*")

    def add_lightweight_component_queried_parameters(self):
        super().add_lightweight_component_queried_parameters()
        self.lightweight_component_queried_category.add_key_value_query("condor_host", "$.config.condor_host")

    def add_advanced_parameters(self):
        super().add_advanced_parameters()

