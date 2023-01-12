#! /bin/bash
if [ -f "~/.ssh/id_rsa_github" ]
then
  echo "rsa key exists, moving on"
else
  ssh-keygen -f ~/.ssh/id_rsa_github -q -N ""
fi

if [ -z "${USERNAME}" ]
then
  echo "USERNAME not defined"
  exit
fi

if [ -z "${EMAIL}" ]
then
  echo "EMAIL not defined"
  exit
fi

git config --global user.name $USERNAME
git config --global user.email $EMAIL
export SSH_TMUX_KEY=`cat ~/.ssh/id_rsa_github.pub`

echo "USERNAME = $USERNAME"
echo "EMAIL = $EMAIL"
echo "SSH_TMUX_KEY = $SSH_TMUX_KEY"

mkdir -p ~/mycode
cd ~/mycode

if [ "$(ls -A ~/mycode)" ]
then
  echo "Your ~/mycode directory is not empty, cowardly refusing to continue!"
  exit
else
  echo "~/mycode is empty, Excellent!"
fi

echo $TOKEN
if [ -z "${TOKEN}" ]
then
  echo "TOKEN not defined"
  exit
fi
curl -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $TOKEN" https://api.github.com/user/repos -d '{"name":"mycode","description":"This is your first repo"}'
curl -X POST -H "Accept: application/vnd.github+json"   -H "Authorization: Bearer $TOKEN"   https://api.github.com/repos/$USERNAME/mycode/keys   -d '{"title":"tmux_key","key":"'"$SSH_TMUX_KEY"'","read_only":false}'

cd ~/mycode
git clone git@github.com:$USERNAME/mycode.git ~/mycode
touch $USERNAME.md
cat <<EOF >> ~/mycode/.gitignore
echo "*.log" >> ~/mycode/.gitignore
echo "*.key" >> ~/mycode/.gitignore
echo "id_rsa*" >> ~/mycode/.gitignore
EOF
git add *
git commit -m "my first commit"
git push origin HEAD
