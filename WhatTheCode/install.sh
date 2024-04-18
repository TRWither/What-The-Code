#!/bin/bash

mkdir -p /usr/local/what-the-code

cp -r * /usr/local/what-the-code

echo 'export PATH=$PATH:/usr/local/what-the-code' >> ~/.bashrc

echo "What The Code successfully installed !"
echo "Don't touch this yellow horse..."
echo "          -- The Potato"

exit 0