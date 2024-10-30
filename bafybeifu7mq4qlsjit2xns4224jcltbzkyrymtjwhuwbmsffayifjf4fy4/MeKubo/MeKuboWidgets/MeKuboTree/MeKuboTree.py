#-----------------------------------------------------------------------
# Name:    MeKuboTree
# Purpose:    MeKuboTree
#
# Author:    me
#
# Created:    2024090216410101
# Copyright:    (c) me 2024090216410101
# Licence:    copyright & all rights reserved
#-----------------------------------------------------------------------
#_____________________________________________________________________
import inspect
import json
import os
import subprocess
import sys
import threading
import time
import traceback
#_____________________________________________________________________
#_____________________________________________________________________
MeCounter0 \
    = \
    0
###timestamper0
##global \
##    MeCounter0
##MeCounter0 \
##    += \
##    1
##if \
##    (
##        MeCounter0 \
##            >= \
##            10000 \
##    ) \
##:
##    MeCounter0 \
##        = \
##        0
##TimeStamper \
##    = \
##    lambda \
##    : \
##    (
##        (
##            int \
##            (
##                time \
##                .time \
##                (
##                )
##            ) \
##            * \
##            (
##                10 \
##                ** \
##                4
##            )
##        ) \
##        + \
##        (
##            MeCounter0 \
##        ) \
##    )
###timestamper1
MeTimeStamper \
    = \
    None
MeSep0 \
    = \
    '    '
MeSep1 \
    = \
    '_'
MeCounter1 \
    = \
    0
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeExceptor \
    (
    ) \
:
    print \
    (
        '\n' \
        + \
        '\n' \
        + \
        ':' \
        + \
        '\n' \
            ,
    )
    traceback \
    .print_exc \
    (
        file \
            = \
            sys \
            .stdout \
    )
    print \
    (
        '\n' \
        + \
        ':' \
        + \
        '\n' \
        + \
        '\n' \
            ,
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeFileWriter \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    try \
    :
        os \
        .makedirs \
        (
            name \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'hashtree' \
                        ,
                ) \
                ,
            exist_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'hashtree' \
                    ,
                MeTimeStamper \
                    ,
            ) \
                ,
            'ab' \
                ,
        ) \
    as \
        FileOpened0 \
    :
        FileOpened0 \
        .write \
        (
            Thing \
            .encode \
            (
                'ascii' \
            )
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGet \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    MePopenProcess00env0 \
        = \
        dict \
        (
        )
    MePopenProcess00env0 \
    .update \
    (
        os \
        .environ \
    )
    MePopenProcess00env0 \
    .update \
    (
        {
            'IPFS_PATH' \
            : \
                os \
                .path \
                .join \
                (
                    '..' \
                        ,
                    '..' \
                        ,
                    'MeKuboWeb3' \
                        ,
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    '.unixfs' \
                        ,
                )
                    ,
        }
    )
    MePopenProcess00args0 \
        = \
        ' ' \
        .join \
        (
            [
                os \
                .path \
                .join \
                (
                    '..' \
                        ,
                    '..' \
                        ,
                    'MeKuboWeb3' \
                        ,
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'dag' \
                    ,
                'get' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MePopenProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MePopenProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
        )
    return \
        MePopenProcess00
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGetJsonLoads \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    return \
        json \
        .loads \
        (
            MeKuboDagGet \
            (
                Thing \
                    = \
                    Thing \
                    ,
            )
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGetTreeMaker \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    global \
        MeCounter1
    MeTree0 \
        = \
        MeKuboDagGetJsonLoads \
        (
            Thing \
                = \
                Thing \
                ,
        )
    MeFileWriter \
    (
        Thing \
            = \
            str \
            (
                MeSep0 \
                * \
                MeCounter1 \
            ) \
            + \
            Thing \
            + \
            '\n' \
            ,
    )
    if \
        'Links' \
    in \
        MeTree0 \
    :
        for \
            x \
        in \
            MeTree0 \
            [
                'Links' \
            ] \
        :
            MeCounter1 \
                += \
                1
            if \
                x \
                [
                    'Name' \
                ] \
                    != \
                    '' \
            :
                MeFileWriter \
                (
                    Thing \
                        = \
                        str \
                        (
                            MeSep1 \
                            * \
                            (
                                128 \
                            ) \
                        ) \
                        + \
                        '\n' \
                        ,
                )
                MeFileWriter \
                (
                    Thing \
                        = \
                        str \
                        (
                            ' ' \
                            * \
                            (
                                127 \
                                - \
                                len \
                                (
                                    x \
                                    [
                                        'Name' \
                                    ] \
                                ) \
                            ) \
                        ) \
                        + \
                        x \
                        [
                            'Name' \
                        ] \
                        + \
                        '\n' \
                        ,
                )
            MeCheckHashTypeOf \
            (
                Thing \
                    = \
                    x \
                    [
                        'Hash' \
                    ] \
                    [
                        '/' \
                    ] \
                    ,
            )
            MeCounter1 \
                -= \
                1
    else \
    :
        return \
            None
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeCheckHashTypeOf \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    if \
        Thing \
            == \
            '' \
    :
        return \
            'none'
    elif \
        Thing \
        [
            0 \
            : \
            7 \
        ] \
            == \
            'bafkrei' \
    :
        MeFileWriter \
        (
            Thing \
                = \
                str \
                (
                    MeSep0 \
                    * \
                    MeCounter1 \
                ) \
                + \
                Thing \
                + \
                '\n' \
                ,
        )
        return \
            'krei'
    else \
    :
        MeKuboDagGetTreeMaker \
        (
            Thing \
                = \
                Thing \
                ,
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeInputter \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    while \
        True \
    :
        print \
        (
            ':' \
                ,
        )
        MeInput0 \
            = \
            input \
            (
                'hash:\n' \
                    ,
            )
        print \
        (
            ':' \
                ,
        )
        #timestamper0
        global \
            MeCounter0
        MeCounter0 \
            += \
            1
        if \
            (
                MeCounter0 \
                    >= \
                    10000 \
            ) \
        :
            MeCounter0 \
                = \
                0
        TimeStamper \
            = \
            lambda \
            : \
            (
                (
                    int \
                    (
                        time \
                        .time \
                        (
                        )
                    ) \
                    * \
                    (
                        10 \
                        ** \
                        4
                    )
                ) \
                + \
                (
                    MeCounter0 \
                ) \
            )
        #timestamper1
        global \
            MeTimeStamper
        MeTimeStamper \
            = \
            MeInput0 \
            + \
            '_' \
            + \
            str \
            (
                TimeStamper \
                (
                )
            ) \
            + \
            '.LOG'
        if \
            MeInput0 \
                != \
                '' \
        :
            MeFileWriter \
            (
                Thing \
                    = \
                    str \
                    (
                        MeSep1 \
                        * \
                        (
                            128 \
                        ) \
                    ) \
                    + \
                    '\n' \
                    ,
            )
        MeInputChecked \
            = \
            MeCheckHashTypeOf \
            (
                Thing \
                    = \
                    MeInput0 \
                    ,
            )
        if \
            MeInput0 \
                != \
                '' \
        :
            MeFileWriter \
            (
                Thing \
                    = \
                    str \
                    (
                        MeSep1 \
                        * \
                        (
                            128 \
                        ) \
                    ) \
                    + \
                    '\n' \
                    ,
            )
        if \
            MeInputChecked \
                == \
                'none' \
        :
            break
        elif \
            MeInputChecked \
                == \
                'krei' \
        :
            continue
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    MeInputter \
    (
    )
except \
:
    pass
#_____________________________________________________________________
