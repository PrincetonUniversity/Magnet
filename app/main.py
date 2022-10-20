import os.path
from PIL import Image
import streamlit as st

from magnet import __version__
from ui_db import ui_core_loss_db
from ui_predict import ui_core_loss_predict
from ui_raw import ui_download_data
from ui_faq import ui_faq
from ui_intro import ui_intro
from magnet.simplecs.simfunctions import SimulationPLECS

STREAMLIT_ROOT = os.path.dirname(__file__)


def ui_multiple_materials(fn, n=1, *args, **kwargs):
    """
    Display multiple instances of input UI widgets, one for each 'material'
      denoted by 'A', 'B', ...
    :param fn: Function or callable that renders UI elements for Streamlit
      This function should take the material identifier ('A', 'B', ..) as the
      first input.
    :param n: Number of times to call `fn`
    :return: None
    """
    for i in range(int(n)):
        fn(chr(ord('A') + i), *args, **kwargs)


def contributor(name, email):
    st.sidebar.markdown(f'<h5>{name} ({email})</h5>', unsafe_allow_html=True)

 
if __name__ == '__main__':

    st.set_page_config(page_title='MagNet', layout='wide')
    st.sidebar.header('Welcome to Princeton MagNet')
    st.sidebar.image(Image.open(os.path.join(STREAMLIT_ROOT, 'img', 'magnetlogo.jpg')), width=300)
    st.sidebar.markdown('by Princeton-Dartmouth-Plexim')
    st.sidebar.markdown('[GitHub](https://github.com/PrincetonUniversity/Magnet) | '
                        '[Princeton Power Electronics](https://www.princeton.edu/~minjie/)')
    function_select = st.sidebar.radio(
        'Select a Function:',
        ('MagNet AI', 'MagNet Visualization', 'MagNet Prediction',
         'MagNet Simulation', 'MagNet Download', 'MagNet Help')
    )

    if 'n_material' not in st.session_state:
        st.session_state.n_material = 1

    if function_select in ['MagNet Visualization', 'MagNet Prediction']:
        clicked = st.sidebar.button("Add Another Case")
        if clicked:
            st.session_state.n_material += 1

    if function_select == 'MagNet AI':
        ui_multiple_materials(ui_intro)
        st.session_state.n_material = 1  # Resets the number of plots

    if function_select == 'MagNet Visualization':
        ui_multiple_materials(ui_core_loss_db, st.session_state.n_material)

    if function_select == 'MagNet Prediction':
        ui_multiple_materials(ui_core_loss_predict, st.session_state.n_material)
        
    if function_select == 'MagNet Simulation':
        st.title('MagNet Simulation - Simulate Magnetics in SPICE')
        ui_multiple_materials(SimulationPLECS)
            
    if function_select == 'MagNet Download':
        ui_multiple_materials(ui_download_data, st.session_state.n_material, streamlit_root=STREAMLIT_ROOT)
        st.session_state.n_material = 1
        
    if function_select == 'MagNet Help':
        ui_multiple_materials(ui_faq)
        st.session_state.n_material = 1  # Resets the number of plots

    st.header('MagNet Research Team')
    st.image(Image.open(os.path.join(STREAMLIT_ROOT, 'img', 'magnetteam.jpg')), width=1000)
    st.header('MagNet Sponsors')
    st.image(Image.open(os.path.join(STREAMLIT_ROOT, 'img', 'sponsor.jpg')), width=1000)

    st.markdown('---')
    st.markdown(f"<h6>MAGNet v{__version__}</h6>", unsafe_allow_html=True)

    st.sidebar.header('Thanks for using MagNet!')
    contributor('Haoran Li', 'haoranli@princeton.edu')
    contributor('Diego Serrano', 'ds9056@princeton.edu')
    contributor('Shukai Wang', 'sw0123@princeton.edu')
    contributor('Annie Lin', 'al2413@princeton.edu')
    contributor('Evan Dogariu', 'edogariu@princeton.edu')
    contributor('Arielle Rivera', 'aerivera@princeton.edu')
    contributor('Yuxin Chen', 'yuxinc@wharton.upenn.edu')
    contributor('Thomas Guillod', 'Thomas.Paul.Henri.Guillod@dartmouth.edu')
    contributor('Vineet Bansal', 'vineetb@princeton.edu')
    contributor('Niraj Jha', 'jha@princeton.edu')
    contributor('Min Luo', 'luo@plexim.com')
    contributor('Charles R. Sullivan', 'charles.r.sullivan@dartmouth.edu')
    contributor('Minjie Chen', 'minjie@princeton.edu')
