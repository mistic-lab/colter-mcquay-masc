
#!/usr/bin/env bash
# Find the source directory of our scripts so we can include our config
SCRIPTS_PATH="$(dirname $0)"
CONFIG_FILE="$SCRIPTS_PATH/scripts.env"
# Source in Configuration
if [ -f $CONFIG_FILE ]; then
  echo "Using Config File"
  . $CONFIG_FILE
else
  echo "Using default config"
  RESULTS_PATH=/home/cjam/Documents/colter-thesis-results
  DATA_PATH=/home/cjam/Documents/colter-thesis/research/data
fi

CMD=$1
case $CMD in
    jupyter)
        echo "Running Jupyter Server"
        echo " Mountin Directories:
        $PWD/research   ->  /home/jovyan/work/
        $PWD/figures    ->  /figures
        $RESULTS_PATH   ->  /results
        $DATA_PATH      ->  /dataset
        "

        docker run --rm -p 8888:8888 \
        -v "$PWD/research":/home/jovyan/work/ \
        -v "$PWD/figures":/figures \
        -v "$RESULTS_PATH":/results \
        -v "$DATA_PATH":/dataset \
        jupyter/scipy-notebook
    ;;
    *)
        echo "
        Available Commands
        ------------------
        jupyter   - Run Jypter Server in this directory
        "
        ;;
esac