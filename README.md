# snapshot-bzr-plugin

## Purpose
I needed simple solution to sync filesystem content with repository.
I use bzr repository to store content of my /etc directory, so after each system update / configuration change I have to add new files to repository or remove from repository files that where deleted. Snapshot-bzr-plugin allows me to use only one bzr command to prepare this synchronization.

Doing snapshot should be should work identically to

* Adding unknown files
* Removing files from `removed` section of `bzr status`
* Commiting those changes and modified files

Example:

    # sudo bzr status /etc
     removed:
       fstab
     modified:
       mail.rc
     unknown:
       fstab.xxx
    # sudo bzr snap /etc -m "System update"
    # sudo bzr status /etc

## Known bugs / limitations

## TODO