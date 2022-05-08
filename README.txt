You will need an environment with Tensorflow to run the Jupyter notebook and python files associated with this tutorial

In case you don't have one, you may create it from our yaml file. Please, run the following commands in your terminal:

# create the environment
cd <path_to_folder_with_yaml_file> # cd Multi-Label Classification/envs
conda env create -f tf_env.yaml

# export it to Jupyter
python -m ipykernel install --user --name=tf_env

The name of the environment is determined in the yaml file. Here, it has been named tf_env.