from restli.generators import PegasusGenerator
from restli.command_line import create_parser
from tests.restli_tests import BaseTest
import os
import mock

class PegasusGeneratorTest(BaseTest):

    def test_it_creates_the_pegasus_file(self):
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()
        generator_args = ['restli', '--generate', 'Fortune', '--namespace', self.package]
        with mock.patch('sys.argv', generator_args):
            generator = PegasusGenerator(create_parser().parse_args())
        generator.generate()
        pegasus_path = os.path.join(self.project_name, 'api', 'src', 'main', 'pegasus', *self.package.split("."))
        self.assertTrue(os.path.exists(os.path.join(self.random_dir, pegasus_path, 'fortune',  "Fortune.pdsc")))

