from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Cyberpunk theme"""
    USERNAME_FG = 124
    USERNAME_BG = 92
    USERNAME_ROOT_BG = 54

    HOSTNAME_FG = 21
    HOSTNAME_BG = 13

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 128  # dark grey
    PATH_FG = 202  # light grey
    CWD_FG = 92  # white
    SEPARATOR_FG = 19

    READONLY_BG = 92
    READONLY_FG = 124

    REPO_CLEAN_BG = 92   
    REPO_CLEAN_FG = 124   
    REPO_DIRTY_BG = 167
    REPO_DIRTY_FG = 93  

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 192
    CMD_PASSED_FG = 93
    CMD_FAILED_BG = 202
    CMD_FAILED_FG = 93

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 0
    VIRTUAL_ENV_FG = 255

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
