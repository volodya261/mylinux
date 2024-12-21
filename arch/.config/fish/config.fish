if status is-login
    if test -z "$DISPLAY" -a "$(tty)" = /dev/tty1
        dbus-run-session Hyprland
    end
end

alias xi='sudo xbps-install -S'
alias lowcpu='sudo $HOME/.config/hypr/cpupower/low-power.sh'
alias defcpu='sudo $HOME/.config/hypr/cpupower/default-cpu.sh'
