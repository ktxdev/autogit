#!/usr/bin/bash
git clone git@github.com:ktxdev/autogit.git
cd autogit
python3 -m venv autogit-venv
source autogit-venv/bin/activate
pip3 install -r requirements.txt
echo "#!/usr/bin/bash" > autogit.sh
echo cd $(pwd) >> autogit.sh
echo 'source  autogit-venv/bin/activate' >> autogit.sh
echo 'python3 autogit.py "$@"' >> autogit.sh
chmod +x autogit.sh
echo "alias autogit=$(pwd)/autogit.sh" >> ~/.bashrc
source ~/.bashrc