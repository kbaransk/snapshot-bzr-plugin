import os

from bzrlib.builtins import tree_files
from bzrlib.commands import Command, display_command, register_command
from bzrlib.errors import PointlessCommit
from bzrlib.option import Option


class cmd_snapshot(Command):
    """Take a snapshot committing the current status.
    """

    takes_args = ['location*']
    takes_options = [Option('message', type=unicode, short_name='m', help="Description of the new revision.")]
    aliases = ['sn', 'snap']

    @display_command
    def run(self, location_list=['.'], message=None):
        for location in location_list:
            #print location
            tree, _ = tree_files([location])
            for relpath in tree.unknowns():
                abspath = os.path.join(location, relpath)
                tree.smart_add([abspath])
            try:
                tree.commit(message, allow_pointless=False, strict=True)
            except PointlessCommit:
                pass

register_command(cmd_snapshot)
