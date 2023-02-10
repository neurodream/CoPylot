env_name=$(head -n 1 environment.yml | sed "s/name: //")

# activate environment
conda activate "$env_name"
# make own package usable
pip install -e .

code .
# TODO clear (?)