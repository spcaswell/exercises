import copy
import stat

import distro
import os
import platform
import shutil

from pathlib import Path
from typing import (Callable, Dict, List, Tuple, Union)


class Utilities:
    cur_platform = platform.system().lower()

    @staticmethod
    def is_linux():
        return Utilities.cur_platform == "linux"

    @staticmethod
    def is_osx():
        return Utilities.cur_platform == "darwin"

    @staticmethod
    def is_windows():
        return Utilities.cur_platform == "windows"

    @staticmethod
    def is_amazon() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "amazon"

    @staticmethod
    def is_arch() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "arch"

    @staticmethod
    def is_debian() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "debian"

    @staticmethod
    def is_openbsd() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "openbsd"

    @staticmethod
    def is_rhel() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "rhel"

    @staticmethod
    def is_ubuntu() -> bool:
        if not Utilities.is_linux():
            return False
        return distro.id().lower() == "ubuntu"

    @staticmethod
    def get_distro() -> Union[str, None]:
        if Utilities.is_linux():
            return distro.id().lower()
        else:
            return None

    @staticmethod
    def list_files(directory_path: Path, recurse: bool = False, show_hidden: bool = True):
        """
        Similar to os.walk(), render a DFS list of files within directory_path by traversing the file hierarchy.
        :param directory_path: str for the path to walk
        :param recurse: If true will continue listing files of subdirectories of folder_path; default = False
        :param show_hidden: If true it will include files marked by the OS as hidden; default = True
        :return: list of file paths
        """
        for p in directory_path.iterdir():
            if not show_hidden and Utilities.is_hidden(p):
                continue
            if p.is_dir():
                if recurse:
                    yield from Utilities.list_files(p, recurse=True)
                else:
                    pass
            else:
                yield p

    @staticmethod
    def list_directories(directory_path: Path, recurse: bool = False, show_hidden: bool = True):
        """
        Similar to os.walk(), render a DFS list of directories within directory_path by traversing the file hierarchy.
        :param directory_path: The root to begin searching from; Path or str accepted
        :param recurse: Boolean; If true will continue listing files of subdirectories of directory_path; default = False
        :param show_hidden:  Boolean; If true will include hidden folders in the results; default = True
        """
        for p in directory_path.iterdir():
            if p.is_file() or (not show_hidden and Utilities.is_hidden(p)):
                continue
            else:
                if recurse:
                    yield from Utilities.list_directories(p, recurse=True, show_hidden=show_hidden)
            yield p

    @staticmethod
    def strip_python_venv() -> Dict[str, str]:
        """
        Creates a copy of the current python virtual environment and strips out all values unique to python virtual
        environments.  When passed to a subprocess this allows the process to execute as if it were not inside a
        python virtual environment.
        :return: new env Dict that can be passed to subprocess.Popen
        """
        new_env = os.environ.copy()
        if Utilities.is_windows():
            if all(["_OLD_VIRTUAL_PATH" not in new_env, "VIRTUAL_ENV" not in new_env]):
                return new_env

            new_env['PATH'] = new_env.pop("_OLD_VIRTUAL_PATH")
            new_env.pop("VIRTUAL_ENV")
        elif Utilities.is_linux():
            if "VIRTUAL_ENV" not in new_env:
                return new_env

            env_paths = [x.strip() for x in new_env['PATH'].split(':') if x.strip()]
            if new_env['VIRTUAL_ENV'] in env_paths[0]:
                new_env['PATH'] = ':'.join(env_paths[1:])
                new_env.pop("VIRTUAL_ENV")
        return new_env

        # TODO: Add OSX support

    @staticmethod
    def find_exe(executable_name, fallback_path: Path = None):
        """
        Finds an executable file using shutil.which().

        :param executable_name: Which executable file to find.
        :param fallback_path: Fallback location to be used if executable is not found.
        :return: str to exe_name
        """
        out = shutil.which(executable_name)
        if out:
            return Path(out)
        else:
            return Path(fallback_path, executable_name)

    @staticmethod
    def recursive_key_search(search_dictionary: Dict, target_key: str, prepend_key: str = "") -> List[Tuple]:
        """
        Search a dictionary with possible nested lists, dicts, and tuples for a key matching, target_key.
        Returns a list of tuples (key_path, value), where key path is a dot (.) separated list of all keys
        accessed to reach the target key and value.  The returned tuple value is the value of the final key/value pair.
        A

        :param search_dictionary: The dictionary to search
        :param target_key: The target_key to search for
        :param prepend_key: A convenience feature that will prepend the supplied string to the final key_path.
        :return: A list of tuples where the final key in the key_path matches the target_key
        [(key_path_0, value_0), (key_path_1, value_1) ... (key_path_n, value_n)]
        """
        kvs_found = []

        for key, value in search_dictionary.items():

            if key == target_key:
                found_key_path = prepend_key + f"{key}"
                kvs_found.append((found_key_path, value))

            elif isinstance(value, dict):
                results = Utilities.recursive_key_search(value, target_key, prepend_key + f"{key}.")
                for result in results:
                    kvs_found.append(result)

            elif isinstance(value, (list, tuple)):
                for item in value:
                    if isinstance(item, dict):
                        results = Utilities.recursive_key_search(item, target_key, prepend_key + f"{key}.")
                        for result in results:
                            kvs_found.append(result)

        return copy.deepcopy(kvs_found)

    @staticmethod
    def collection_leaf_map(node: Union[dict, list, set, tuple, Callable], func: Callable, ignore_dict=False,
                            ignore_list=False, ignore_set=False, ignore_tuple=False):
        """
        Performs a depth first walk of a collection and applies func to all non-collection objects contained inside the
        root collection.  It will inspect all nested collections for non-collection type objects.  Returns a copy of the
        root collection with all non-collection objects modified by func.  The different base collections are dict, list,
        set, and tuple.  Each can be selectively disabled with the ignore_[type] parameters.

        :param node: The Collection object to walk
        :param func: The function to map to all non-collection objects in the walked collection
        :param ignore_dict: Flag to ignore dictionary objects
        :param ignore_list: Flag to ignore list objects
        :param ignore_set: Flag to ignore set objects
        :param ignore_tuple: Flag to ignore tuple objects
        :return: A collection with all non-collection objects modified by func
        """

        if isinstance(node, dict):
            if ignore_dict:
                return node
            else:
                return {k: Utilities.collection_leaf_map(v, func) for k, v in node.items()}
        if isinstance(node, list):
            if ignore_list:
                return node
            else:
                return [Utilities.collection_leaf_map(x, func) for x in node]
        if isinstance(node, set):
            if ignore_set:
                return node
            else:
                return {Utilities.collection_leaf_map(s, func) for s in node}
        if isinstance(node, tuple):
            if ignore_tuple:
                return node
            else:
                return tuple(Utilities.collection_leaf_map(t, func) for t in node)
        else:
            return func(node)

    @staticmethod
    def is_hidden(file_path: Path, ) -> bool:
        """
        Returns True if the file or directory at file_path is marked hidden by the OS or by posix leading '.' convention.
        Assumes object at file_path is not hidden if no explicit check returns True.
        @param file_path: The path to the file to check.
        @return: True if the file should be considered a hidden file.
        """
        if Utilities.is_linux():
            if file_path.name.startswith('.'):
                return True
        elif Utilities.is_windows():
            return file_path.stat().st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN != 0
        elif Utilities.is_osx():
            from osx import is_hidden as osx_is_hidden
            # Fuck Apple... Check filename, HFS Invisible Flag, Finder Hidden Flag, special blacklist in CoreFoundation
            if file_path.name.startswith('.'):
                return True
            # HFS Flag
            stat_info = file_path.lstat()
            hidden_flag = getattr(stat_info, 'st_flags', 0) & getattr(stat_info, 'UF_HIDDEN') != 0
            if hidden_flag:
                return True
            else:
                # I'm not sure if this checks the blacklist or not, but the list changes in each OSX version, and there
                # is no guarantee the damn blacklist file will stay in the same place. This is a best guess implementation.
                try:
                    return osx_is_hidden(file_path)
                except OSError:
                    # Fuck it I don't care if it's supposed to be hidden at this point
                    return False
        return False
