export PATH="/usr/local/opt/php@7.2/bin:$PATH"
export PATH="/usr/local/opt/php@7.2/sbin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Git
alias gs='git status'
alias gl='git log'
alias gd='git diff'
alias gd1='~/codebase/dotfiles/git-diff-first-modified-file.sh'
alias ga='git add'
alias ga1='~/codebase/dotfiles/git-add-first-modified-file.sh'
alias gc='git commit -m'

# Supercuts
alias _b='~/codebase/dotfiles/git-current-branch-name-to-clipboard.sh'
alias _n='ncmpcpp'

# Apps
alias pngr='python ~/codebase/pngr/pngr.py'
alias track='python ~/codebase/dotfiles/track.py'
alias lsa='ls -alh'
alias emacs='emacs -nw'
alias python='python3'

# Wayfair
alias wf2='wf'
alias wf='wf3'
alias cdah='cd /wayfair/data/codebase/php/applications/customer-experience/service-agent-hub'

export PATH=/Users/vjacek/bin:$PATH # needed for wf3
export FPATH="/Users/vjacek/.wf/zsh-completion:$FPATH"
compinit
export PATH="~/bin:$PATH"
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
