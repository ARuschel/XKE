#!/bin/bash

(cd /home/andrey/proj/XKE/pra/; sbt "runMain edu.cmu.ml.rtw.pra.experiments.ExperimentRunner $1 $2")
