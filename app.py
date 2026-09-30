import streamlit as st
from pathlib import Path
import base64
import html

st.set_page_config(
    page_title="TOOBA.exe — The Mystery Machine",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

FINAL_NOTE = """Tooba,

This little archive isn't a test of how well you remember things.

It is just a small place made to remind you that your presence has mattered.

Some days were ordinary. Some were completely chaotic. Some moments probably meant nothing at the time — and somehow became memories anyway.

So if you ever wonder whether you made a difference in someone's life:
yes, you did.

Thank you for being part of the story. 🤍
"""

CLUES = [
    ("THE BEGINNING", "Every good archive has an origin story.", "Somewhere between ordinary days and random conversations, the memories started collecting themselves."),
    ("THE CHAOS", "Evidence suggests: things were not always normal.", "There were laughs, weird moments, unexpected conversations and the kind of chaos that becomes funny later."),
    ("THE LITTLE THINGS", "The smallest moments usually survive the longest.", "A message. A joke. A shared moment. A day that looked ordinary until it became a memory."),
]

def init_state():
    for key, value in {
        "screen": 0, "clues": set(), "final_unlocked": False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_state()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
.stApp{background:radial-gradient(circle at 15% 10%,rgba(139,92,246,.18),transparent 30%),radial-gradient(circle at 90% 70%,rgba(45,212,191,.10),transparent 28%),#08080d;color:#f4f1f8}
.block-container{max-width:1080px;padding:42px 24px 70px}
.hero{min-height:68vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.kicker,.eyebrow{font:500 11px 'DM Mono',monospace;letter-spacing:3px;color:#9ff2d0;text-transform:uppercase}
.title{font:600 clamp(64px,12vw,145px) 'Playfair Display',serif;line-height:.9;margin:16px 0;letter-spacing:-5px}
.subtitle{max-width:680px;color:#aaa5b5;font:600 16px 'Manrope',sans-serif;line-height:1.7}
.panel{background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.12);border-radius:24px;padding:28px;backdrop-filter:blur(14px);margin:18px 0}
.card-title{font:800 25px 'Manrope',sans-serif;margin:8px 0}
.body{color:#aaa5b5;line-height:1.75;font:500 15px 'Manrope',sans-serif}
.quote{font:italic 23px 'Playfair Display',serif;line-height:1.5}
.media-card{overflow:hidden;border-radius:24px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.035);margin:18px 0;box-shadow:0 20px 70px rgba(0,0,0,.25)}
.media-card img{width:100%;display:block;max-height:720px;object-fit:cover}
.media-caption{padding:16px 19px;color:#d9d4df;font:700 13px 'Manrope',sans-serif;letter-spacing:.3px}
.lock{text-align:center;padding:65px 20px}
.footer{text-align:center;color:#6e6877;font:500 11px 'DM Mono',monospace;margin-top:55px;letter-spacing:1px}
div.stButton>button{border:1px solid rgba(255,255,255,.12);border-radius:14px;background:rgba(255,255,255,.06);color:#f4f1f8;font-weight:700;min-height:48px}
div.stButton>button:hover{border-color:rgba(182,156,255,.7);background:rgba(182,156,255,.12)}
@media(max-width:650px){.block-container{padding:25px 14px 50px}.title{letter-spacing:-3px}.panel{padding:20px;border-radius:20px}}
</style>
""", unsafe_allow_html=True)

def go(n):
    st.session_state.screen = n
    st.rerun()

def img_b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()

# SCREEN 0
if st.session_state.screen == 0:
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">private archive // file 001</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">TOOBA.exe</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A tiny interactive archive of clues, memories, little things and a few pieces of evidence worth keeping.<br>Proceed only if you are ready to open the file.</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("✦  ENTER THE ARCHIVE", use_container_width=True):
        go(1)
    st.markdown('</div>', unsafe_allow_html=True)

# SCREEN 1
elif st.session_state.screen == 1:
    st.markdown('<div class="kicker">identity check</div><h1>Before the archive opens…</h1>', unsafe_allow_html=True)
    questions = [
        ("01","What kind of person is Tooba?",["A little chaotic","Quietly unforgettable","Both. Obviously."]),
        ("02","What makes an ordinary day memorable?",["A random laugh","A tiny inside joke","The people in it"]),
        ("03","What should every great friendship contain?",["Trust","Chaos","A ridiculous number of memories"]),
    ]
    for code,q,opts in questions:
        st.radio(q,opts,horizontal=True,key=f"q{code}")
    if st.button("UNLOCK THE FIRST CLUE →",use_container_width=True):
        go(2)

# SCREEN 2
elif st.session_state.screen == 2:
    st.markdown('<div class="kicker">archive / clues</div><h1>Three files were found.</h1>',unsafe_allow_html=True)
    for i,(name,sub,body) in enumerate(CLUES):
        st.markdown(f'<div class="panel"><div class="eyebrow">CLUE 0{i+1}</div><div class="card-title">{name}</div><div class="body">{sub}</div>',unsafe_allow_html=True)
        if st.button(f"OPEN CLUE 0{i+1}",key=f"c{i}"):
            st.session_state.clues.add(i)
            st.rerun()
        if i in st.session_state.clues:
            st.markdown(f'<div class="quote">“{body}”</div></div>',unsafe_allow_html=True)
        else:
            st.markdown('</div>',unsafe_allow_html=True)
    if len(st.session_state.clues)==3 and st.button("ENTER THE MEMORY VAULT →",use_container_width=True):
        go(3)

# SCREEN 3
elif st.session_state.screen == 3:
    st.markdown('<div class="kicker">memory vault</div><h1>Recovered memories.</h1>',unsafe_allow_html=True)
    st.markdown('<p class="body">Two moments were recovered and cleaned up from the supplied screenshots. They are presented as part of the archive — no upload controls, no media picker.</p>',unsafe_allow_html=True)

    for name, caption in [
        ("memory_01.jpg","THE MOMENT — 01"),
        ("memory_02.jpg","THE MOMENT — 02")
    ]:
        p=ASSETS/name
        st.markdown(f'<div class="media-card"><img src="{img_b64(p)}"><div class="media-caption">{caption}</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="panel"><div class="eyebrow">VIDEO REEL</div><div class="card-title">A small moving memory</div><div class="body">This reel was created from the two supplied frames because the original video file was not included in the uploads.</div></div>',unsafe_allow_html=True)
    st.video(str(ASSETS/"memory_reel.mp4"))

    if st.button("CONTINUE →",use_container_width=True):
        go(4)

# SCREEN 4
elif st.session_state.screen == 4:
    st.markdown("<div class='kicker'>the little things</div><h1>Things that don't need a big explanation.</h1>", unsafe_allow_html=True)
    items=[
        ("01","RANDOM MOMENTS","The moments nobody planned often become the ones worth keeping."),
        ("02","THE CHAOS","Not everything has to make sense to become a good memory."),
        ("03","ORDINARY DAYS","Sometimes an ordinary day becomes special only because of who was there."),
        ("04","THE ARCHIVE","Two moments, one little reel, and everything else that makes a memory feel like a memory."),
    ]
    for code,name,body in items:
        st.markdown(f'<div class="panel"><div class="eyebrow">{code}</div><div class="card-title">{name}</div><div class="body">{body}</div></div>',unsafe_allow_html=True)
    if st.button("OPEN THE FINAL FILE →",use_container_width=True):
        go(5)

# SCREEN 5
else:
    st.markdown('<div class="kicker">final file</div>',unsafe_allow_html=True)
    if not st.session_state.final_unlocked:
        st.markdown('<div class="lock"><div style="font-size:55px">🔒</div><h1>FINAL_FILE.txt</h1><p class="body">One last confirmation. The archive is almost complete.</p></div>',unsafe_allow_html=True)
        if st.button("DECRYPT FINAL FILE",use_container_width=True):
            st.session_state.final_unlocked=True
            st.rerun()
    else:
        st.markdown('<div class="panel"><div class="quote">'+html.escape(FINAL_NOTE).replace("\n","<br><br>")+'</div></div>',unsafe_allow_html=True)
        st.balloons()
        if st.button("↻ RESTART EXPERIENCE",use_container_width=True):
            for k in ["screen","clues","final_unlocked"]:
                st.session_state.pop(k,None)
            st.rerun()

st.markdown('<div class="footer">TOOBA.exe // built with Streamlit // no AI required</div>',unsafe_allow_html=True)
                
