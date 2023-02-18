
import streamlit as st
import base64
from PIL import Image
import time
st.set_page_config(layout="wide",page_title="Anuj Mishra",page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f468-1f3fc-200d-1f393.png")

def set_background(png_file):
    bg_img = '''
    <style>
    .stApp {
    background-image: url("%s");
    background-size: contain;
    }
    </style>
    '''%png_file
    st.markdown(bg_img, unsafe_allow_html=True)
set_background('https://i.ibb.co/yS6JpW1/OIP-2.jpg')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
page_bg_img = '''

<p align="center">
  <a href="https://github.com/Anuj-gr8/Anuj-gr8/"><img src="https://readme-typing-svg.herokuapp.com?lines=Computer+Science+Student;AI-ML%20Enthusiast;Cafephile;Always%20learning%20new%20things;Evolving&center=true&width=500&height=50"></a>
</p>
<p align='center'><em><b>Find yourself to discover the real you.</b></em>
<br/>
<em><b>- Key words of the life</b></em>
'''
page_bg_img1 = '''

<br />
</h1>

<p align='center'><em><b>Coming together is a beginning; keeping together is progress; working together is success.</b></em>
<br/>
 <em><b>- Henry Ford</b></em>
<br><br/>
'''
page_footer = '''
<br><br>
### Reach me:
[![Instagram](https://img.shields.io/badge/-Instagram-c13584?style=flat&labelColor=c13584&logo=instagram&logoColor=white&align=center)](https://www.instagram.com/anuj_mishra028/)
[![Twitter Follow](https://img.shields.io/twitter/follow/Anujmishra27003?color=1DA1F2&logo=twitter&style=flat&align=center)](https://twitter.com/Anujmishra27003?t=uUCjGiuVtJgVozF71iMVOQ&s=08)
[![Linkedin](https://img.shields.io/static/v1?label=&message=Linkedin&color=0E7FBF&&&style=flat&logo=linkedin&logoColor=white&align=center)](https://www.linkedin.com/in/anuj-mishra-500320216/)
[![Medium](https://img.shields.io/website?label=Medium&style=flat&url=https%3A%2F%2Fwww.medium.com%2Fprofile%2Fanuj-mishra&align=center)](
https://anuj-mishra.medium.com/)
[![Github](https://img.shields.io/badge/-Github-c13584?style=flat&labelColor=c13584&logo=github&logoColor=white&align=center)](https://github.com/Anuj-gr8/Anuj-gr8)

'''
work_spaces = '''
<p align='center'>
<br/><br/>
  <!-- <img alt="os" src="https://img.shields.io/badge/Apple-Acer_Nitro_5-999999?style=flat&logo=apple&logoColor=white" /> -->
  <img alt="os" src="https://img.shields.io/badge/Windows-11_5-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  <img alt="soc" src="https://img.shields.io/badge/Intel-Core_i5-0071C5?style=for-the-badge&logo=intel&logoColor=white" />
  <img alt="ram" src="https://img.shields.io/badge/RAM-8GB-%230071C5.svg?&style=for-the-badge&logoColor=white" /><br><br>
  <img alt="graphics" src="https://img.shields.io/badge/NVIDIA-GTX1650-76B900?style=for-the-badge&logo=nvidia&logoColor=white" />
  <img alt="ssd" src="https://img.shields.io/badge/256%20GB%20SSD-grey?style=for-the-badge" />
  <img alt="hdd" src="https://img.shields.io/badge/1%20TB%20HDD-grey?style=for-the-badge" />
</p>
<br/><br/>
'''
soft ='''
<p align='center'>
<br><br>
<img src="https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white" />
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" /><br><br>
<img src="https://img.shields.io/badge/Microsoft_Office-D83B01?style=for-the-badge&logo=microsoft-office&logoColor=white" />
<img src="https://img.shields.io/badge/PyCharm-D83B65?style=for-the-badge&logo=PyCharm&logoColor=red"/>
</p>
<br/><br/>
'''
projects ='''
<p align='center'>
<br><br>
<h5>Handwriting Cheracter and digit recognition: 👉
<a href="https://github.com/Anuj-gr8/APLHA_NUM" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/ALFANUM-2C2255?style=for-the-badge&logo=alfanum&logoColor=white" /></a></h5><br>
<h5>Building Browser with python: 👉
<a href="https://github.com/Anuj-gr8/my-browser" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/MY_Browser-0078D4?style=for-the-badge&logo=my%20sBrowser&logoColor=white" /></a></h5><br>
<h5>Ecom/EdTech Chatbot : 👉
<a href="https://github.com/Anuj-gr8/Edtech_chatbot" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/ChatBot-3C7755?style=for-the-badge&logo=Chatbot&logoColor=white" /></a></h5><br>
<h5>Play-lang: 'A Tool to doing some language tasks' 👉
<a href="https://github.com/Anuj-gr8/Play_lang" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/PlayLang-D83B01?style=for-the-badge&logo=PlayLang&logoColor=white" /></a></h5><br>
<h5>Py_Site: 'A portfolio website built by python' 👉
<a href="https://github.com/Anuj-gr8/mywebsite" target="_blank" rel="noreferrer">
<img src="https://img.shields.io/badge/mywebsite-D83B65?style=for-the-badge&logo=mywebsite&logoColor=red"/></a></h5><br>
</p>
<br/><br/>
'''
Skills ='''
<p align='center'>
<a href="https://www.python.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="30" alt="vscode" /></a>
<a href="https://docs.microsoft.com/en-us/cpp/?view=msvc-170" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" height="30" alt="C" /></a>
<a href="https://docs.microsoft.com/en-us/cpp/?view=msvc-170" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" height="30" alt="C++" /></a>
<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" height="30" alt="CSS3" /></a>
<a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" height="30" alt="HTML5" /></a>
<a href="https://www.oracle.com/java/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" height="30" alt="Java" /></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" height="30" alt="MySQL" /></a>
<a href="https://desktop.github.com/" target="_blank" rel="noreferrer"><img src="https://avatars.githubusercontent.com/u/13171334?s=200&v=4" height="30" alt="githubdesktop" /></a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" height="30" alt="git" /></a>
<a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1024px-Visual_Studio_Code_1.35_icon.svg.png" height="30" alt="vscode" /></a>

</p>
<br/><br/>
'''
resume = '''
    <iframe src="https://publuu.com/flip-book/88007/244547" width="100%" height="500px">
    </iframe>
'''
extra = '''
<h4 style='text-align: center; color: red;'><a href='https://mstcvitbhopal.live'>Currently I am the Technical team head of the Microsoft Technical Club VIT BHOPAL</a></h4>
'''
Contact = '''
<br><br>
[![WhatsApp](https://img.shields.io/badge/-WhatsApp-D18984?style=flat&labelColor=c13584&logo=WhatsApp&logoColor=white&align=center)](https://wa.link/t06alh)
[![Eamil](https://img.shields.io/badge/E--mail-G--mail-blue?&logo=G-mail&style=flat&align=center)](mailto:anujmishra282003@gmail.com)
[![Call](https://img.shields.io/badge/-Call-E19084?style=flat&labelColor=c13584&logo=Call&logoColor=white&align=center)](tel:+918839219481)

'''
img = '''
<a><img src="https://i.ibb.co/7X94fYV/my-image1.png" alt="my image" width="250" height="250"></a>
'''
st.markdown("<h1 style='text-align: center; color: red;'><a href='https://git.io/typing-svg'><img src='https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=37&duration=2500&pause=1000&color=89E94E&background=5730FF00&width=435&lines=Hey,+I+am+Anuj+🙋‍♂️' alt='Typing SVG' /></a></h1>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])
with tab1:
    with st.spinner('Wait for it...'):
        time.sleep(2)
    # image = Image.open("https://www.bing.com/images/search?q=Google+Upload+Icon&FORM=IRIBIP")
    col1, col2 = st.columns([3, 1])
    with col1.container():
        st.markdown(page_bg_img1, unsafe_allow_html=True)
        st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("Hi, I'm Anuj Mishra, a passionate self-taught web developer and AI enthusiast from India. My passion for software lies in dreaming up ideas and making them come true with elegant interfaces."+ 
    "\nI take great care in the experience, architecture, and code quality of the things I build. I'm 20 years old and graduated with a degree in Integrated M.Tech. with CSE specialization in AI&ML VIT BHOPAL UNIVERSITY.\nI'm also an open-source enthusiast. I learned a lot from the open-source community and I love how collaboration and knowledge sharing happened through open-source.")

    with col2.container():
        st.markdown(img, unsafe_allow_html=True)
with tab2:
    st.balloons()
    st.write("## About")
    with st.expander("🏆🏆Skils🏆🏆"):
        st.markdown(Skills, unsafe_allow_html=True)
    with st.expander("💻 My workspace"):
        st.markdown(work_spaces, unsafe_allow_html=True)
    with st.expander("⚙️ Softwares I'm Familiar with :"):
        st.markdown(soft, unsafe_allow_html=True)
    with st.expander("📽️ Major Projects:"):
        st.markdown(projects, unsafe_allow_html=True)
    with st.expander("Resume:📑"):
        st.markdown(resume, unsafe_allow_html=True)
    with st.expander("Extra curriculurm:"):
        st.markdown(extra, unsafe_allow_html=True)
    
with tab3:
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success("## Contact me")
    progrs = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        progrs.progress(i+1)
    st.markdown(Contact, unsafe_allow_html=True)
st.write()
st.write()
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write(" \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 
st.markdown(page_footer, unsafe_allow_html=True)
