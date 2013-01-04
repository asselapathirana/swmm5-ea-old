# chardet's setup.py
from distutils.core import setup
import itertools
from swmm5ea import swmm_ea_controller as sc

EXAMPLES=("storage_example", "simple_reservoir_and_pipe_example", "watershed_calibration")
EXTS=["inp", "inp_", "yaml", "cal"]
EXTS.extend([x.upper() for x in EXTS])
EXAMPLES=list(itertools.product(EXAMPLES,EXTS))
package_data=[ "examples/"+x[0]+"/*."+x[1] for x in EXAMPLES]
#package_data.append("*.pyw")
print package_data
setup(
    name = sc.NAME,
    packages = ["swmm5ea"],
    package_data={'swmm5ea': package_data},
    version = sc.VERSION,
    description = sc.DESCRIPTION,
    author = sc.AUTHOR,
    license=sc.LICENSE,
    #publisher=sc.PUBLISHER,
    author_email = sc.EMAIL,
    url = sc.URL,
    download_url = sc.DLURL,
    keywords = ["EPA-SWMM", "GA", "Urban Drainage"],
    classifiers = sc.CLASSIFY,
    long_description = sc.LONGDISC
)