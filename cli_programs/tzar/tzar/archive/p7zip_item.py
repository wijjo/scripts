# Copyright 2016-17 Steven Cooper
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""P7Zip-compressed archive item."""

#pylint: disable=import-error
from scriptbase import console

from .base_item import BaseItem

class P7ZipItem(BaseItem):
    """P7Zip-compressed archive item."""

    @classmethod
    def item_for_path_if_matching(cls, path, parsed_name, config_data, **kwargs):
        """Create an archive item if it has the appropriate extension."""
        if parsed_name.extension == '7z':
            return P7ZipItem(path, config_data, **kwargs)

    def __init__(self, path, config_data, **kwargs):
        """Construct archive item."""
        BaseItem.__init__(self, path, config_data, **kwargs)

    def build_create_batch(self, batch):
        """Populate a command batch for creating the archive."""
        batch.add_command('7za', 'a')
        batch.add_exclude_args('-xr!')
        batch.add_args((self.archive, '.7z'), self.path)
        batch.add_source_deletion()

    def build_restore_batch(self, batch):   #pylint: disable=no-self-use,unused-argument
        """Populate a command batch for restoring the archive."""
        console.abort('Restore is not yet implemented for p7zip compression.')

    def build_compare_batch(self, batch):   #pylint: disable=no-self-use,unused-argument
        """Populate a command batch for comparing against the archive."""
        console.abort('Compare is not yet implemented for p7zip compression.')
