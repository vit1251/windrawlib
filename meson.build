project('WinDrawLib', 'c', version: '3.1')

inc_dir = include_directories('include', 'src/c-win32/include')

# Enable COM interface preprocessor wrapper macros for C.
#-DCOBJMACROS
#-DDEBUG

#if COMPILER == GNUCC
#    # Detect gcc version:
#    # Enable many warnings:
#    -Wall -Wdouble-promotion
#    # Use unicode (-W suffixed symbols):
#    -municode
#    # Use faster but less precise float math; it suffices for our purposes:
#    -ffast-math
#    # Lets stick with safer -O2
#    -O2

#if COMPILER == MSVC
#    # Disable warnings about the so-called unsecured functions:
#    /D_CRT_SECURE_NO_WARNINGS
#    # Use faster but less precise float math; it suffices for our purposes:
#    /fp:fast
#    # Specify proper C runtime library:
#    /MTd
#    /MT


sources = [
    'src/backend-d2d.c',
    'src/backend-dwrite.c',
    'src/backend-gdix.c',
    'src/backend-wic.c',
    'src/bitblt.c',
    'src/brush.c',
    'src/cachedimage.c',
    'src/canvas.c',
    'src/draw.c',
    'src/fill.c',
    'src/font.c',
    'src/image.c',
    'src/init.c',
    'src/memstream.c',
    'src/misc.c',
    'src/path.c',
    'src/string.c',
    'src/strokestyle.c',
]

windrawlib = static_library('windrawlib', sources,
        include_directories: [ inc_dir ],
        c_args: [ '-DUNICODE', '-D_UNICODE', '-D_WIN32_IE=0x0501', '-D_WIN32_WINNT=0x0600', '-DWINVER=_WIN32_WINNT' ],
    )

###
### Examples
###

