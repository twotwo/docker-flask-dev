export LS_OPTIONS='--color=auto'
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls $LS_OPTIONS'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep $LS_OPTIONS'
    alias fgrep='fgrep $LS_OPTIONS'
    alias egrep='egrep $LS_OPTIONS'
fi
# some more ls aliases
alias ll='ls -l'
alias la='ls -A'