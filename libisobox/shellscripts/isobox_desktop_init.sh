

if command -v "pipewire" &> /dev/null && command -v "pipewire-pulse" &> /dev/null
then

    pipewire &
    pipewire-pulse &
    dbus-launch wireplumber &

elif command -v "pulseaudio" &> /dev/null
then
    pulseaudio &
fi

