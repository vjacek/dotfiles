export PATH="/usr/local/opt/php@7.2/bin:$PATH"
export PATH="/usr/local/opt/php@7.2/sbin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

export FPATH="/Users/vjacek/.wf/zsh-completion:$FPATH"
compinit
export PATH="~/bin:$PATH"



alias lsa='ls -alh'
alias emacs='emacs -nw'
alias python='python3'

alias gs='git status'
alias gl='git log'
alias gd='git diff'
alias ga='git add'
alias gc='git commit -m'

alias _b='~/codebase/dotfiles/git-current-branch-name-to-clipboard.sh'
alias _n='ncmpcpp'

alias pngr='python ~/codebase/pngr/pngr.py'
alias track='python ~/codebase/dotfiles/track.py'
