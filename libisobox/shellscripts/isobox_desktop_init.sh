

if command -v "pipewire" &> /dev/null && command -v "pipewire-pulse" &> /dev/null
then
    #XDG Runtime dir has to be set for this to work
    unset XDG_RUNTIME_DIR
    export XDG_RUNTIME_DIR=$(mktemp -d /tmp/$(id -u)-runtime-dir.XXX)
    pipewire &
    pipewire-pulse &
    dbus-launch wireplumber &
elif command -v "pulseaudio" &> /dev/null
then
    pulseaudio &
fi

