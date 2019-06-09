#!/usr/bin/env bash -e


PYTHON=`which python3`
VENV=venv

if [ -f "$PYTHON" ]
then

    if [ ! -d $VENV ]
    then
        # Create a virtual environment if it doesn't exist.
        $PYTHON -m venv $VENV
    else
        if [ -e $VENV/bin/python2 ]
        then
            # If a Python2 environment exists, delete it first
            # before creating a new Python 3 virtual environment.
            rm -r $VENV
            $PYTHON -m venv $VENV
        fi
    fi

    # Activate the virtual environment and install requirements.
    . $VENV/bin/activate
    pip3 install -r requirements.txt

	# make actions executable
	chmod +x /var/lib/snips/skills/snips-music-actions/action-music.py /var/lib/snips/skills/snips-music-actions/action-spotify.py
else
    >&2 echo "Cannot find Python 3. Please install it."
fi