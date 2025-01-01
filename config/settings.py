import os

# API keys and environment variables
os.environ.update({
    'PYTHONWARNINGS': 'ignore',
    'FLAGS_logtostderr': '0',
    'GLOG_minloglevel': '2',
    'TF_CPP_MIN_LOG_LEVEL': '2'
})

GOOGLE_API_KEY = ""
USE_GPU = True
