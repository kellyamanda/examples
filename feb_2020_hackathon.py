import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import math, urllib, requests

st.sidebar.subheader('Welcome to the App')
app_mode = st.sidebar.radio('Select mode', ('Explanation', 'App tips', 'App example', 'Source code'))

if app_mode == 'Explanation':
    st.write('''
    ## Welcome to Streamlit

    Here are some tips for creating a demo to show off your work.

    First, create an explanation section like this. Remember that whoever you are showing your project
    to has no context for your work, so let them know a little about what you're doing.

    👈👈 To keep it clean use `st.sidebar` to create a different section for your explanation and your app.

    ### What to put in your explanation

    - What is your project trying to achieve?
    - What is the benefit to an end user of the project?
    - What is your methodology?

    If there's a lot of information, break it up into sections using `st.subheader` or you can use
    markdown with `st.write('##Text here')`.
    ''')

elif app_mode == 'App tips':

    st.sidebar.subheader('App inputs')
    select_size = st.sidebar.selectbox('Choose header type', [3, 2, 1])
    subheader_size = '#' * select_size

    st.write(subheader_size, 'Tip 1: Show off your work')
    st.write('''Your project needs visuals, whether that\'s a video, audio clip, image, map, chart, or table. Streamlit supports
    all major charting libraries. Check out [docs.streamlit.io](http://docs.streamlit.io) to explore all the options.''')

    data = [15, 10, 7]
    labels = ['Good', 'Bad', 'Ugly']

    fig = go.Figure(data=[go.Pie(labels=labels, values=data, hole=.5)])
    fig.update_layout(
        autosize=False,
        width=500,
        height=300)
    st.write(fig)

    '-------------------'

    st.write(subheader_size, 'Tip 2: Make it interactive')
    st.write('''Any variable can be made interactive by using a widget. Use widgets like `st.slider`, `st.selectbox`, and `st.radio`
    to let users of your app change parameters, select different inputs, or modify the output.
    ''')
    number = st.number_input('Number', value=1)
    exponent = st.slider('Exponent',1,100)
    output = number ** exponent
    st.write(number, ' to the power of ', exponent, ' equals ', output)

    '-------------------'

    st.write(subheader_size, 'Tip 3: Move widgets to sidebar')
    st.write('''By adding `st.sidebar` to any of your widgets you can move them to the sidebar on the left. This
    cleans up the layout and makes sure that your controls are always visible. _Note: some widgets are best
    left inline, especially if they only control one small part of the app._
    ''')

    sidebar_code = (
    '''
    st.sidebar.subheader('App inputs')
    select_size = st.sidebar.selectbox('Choose header type', [3, 2, 1])
    ''')

    st.code(sidebar_code, language='python')

    st.write('#### 👈👈 &nbsp; use the selectbox to change the header types!')

    '-------------------'

    st.write(subheader_size, 'Tip 4: Add some text')
    st.write('''Write out the important parts that need explanation or use text to break up the layout of the app.
    Have a friend play with the app and tell you what isn't obvious, so you can add text for those sections.
    If you want to add text in the sidebar use `st.sidebar.subheader` or `st.sidebar.text`.''')

    '-------------------'

    st.write(subheader_size, 'Tip 5: Hide extra text')
    st.write('''To keep your app layout clean, you can add in explanations or extra info, graphs, etc. by hiding
    that information behind a checkbox or a selectbox. See two examples below.''')

    st.write('###')

    if st.checkbox('Show explanation'):
        st.write('''
            > ###### We balance probabilities and choose the most likely. It is the scientific use of the imagination, but we have always some material basis on which to start our speculation. - Sherlock Holmes
            ''')

    st.write('###')

    selectbox = st.selectbox('Show more analyses', ('','Raw data', 'Extra chart'))

    data = np.random.rand(3,2)

    if selectbox == 'Raw data':
        st.table(data)
    elif selectbox == 'Extra chart':
        st.line_chart(data)

    '-------------------'

    st.write(subheader_size, 'Tip 6: Use caching to speed up your app')
    st.write('''You want the app to run quickly for your users, so use `st.cache` for any expensive
    computation or data pulls. Read more about [how st.cache works](https://docs.streamlit.io/caching.html)
    and check out [documentation on advanced caching](https://docs.streamlit.io/advanced_caching.html)
    for how use `st.cache` to store a TensorFlow object or read from a MySQL database''')

    '-------------------'

    st.write(subheader_size, 'Tip 7: Put the good stuff at the top')
    st.write('''If your project is a step by step walk through - then ignore this. If it\'s an app for someone to used, then you want
    to get them to the good, interactive stuff as soon as possible. This also means setting your app to have a default good outcome
    that users can see first before interacting with the app.''')

    dog_img = 'https://www.publicdomainpictures.net/pictures/240000/velka/funny-dog-15091160994Oj.jpg'
    with st.echo():
        show_image = st.empty()
        if st.checkbox('Show image', value=True):
            show_image.image(dog_img, width=250)

    st.write('''One way you can do that is with `st.empty`, which allows you to choose the order of where elements appear in the app.
    In the example above the code for the checkbox has to come before the image, but we can use `st.empty` to have the image render
    above the checkbox.''')

    '-------------------'

    st.write(subheader_size, 'Tip 8: Show some code (maybe)')
    st.write('''If you're teaching a concept it can be useful to show off some code. If it's codd not used in your app you can use `st.code`, but
    if you want to show the code for something you are doing in the app you can use `with st.echo()` to have code shown inline with output.
    ''')

    with st.echo():
        tasty = 'nom '
        st.write(tasty * 3)


    '-------------------'
    st.write(subheader_size, 'Tip 9: Do something delightful')
    st.write('''Whenever possible try to use more exciting or fun examples, or for bonus points, add an
    unexpected and memorable interaction.
    ''')
    if st.button('Balloons!!!'):
        st.balloons()


elif app_mode == 'App example':

    st.header('Playing With Famous Paintings')

    st.sidebar.subheader('App options')
    img_select = st.sidebar.selectbox('Choose painting', ('Nighthawks', 'Starry Night', 'The Persistence of Memory'))
    treatment_select = st.sidebar.selectbox('Choose treatment', ('None','Gold frame','Color tint', 'Flip image'))

    # Assigning URL and captions to image selection
    if img_select == 'Nighthawks':
        caption = 'Nighthawks by Edward Hopper'
        img_url = 'https://cdn.britannica.com/42/19342-050-1034FC73/Nighthawks-oil-canvas-Edward-Hopper-Art-Institute-1942.jpg'
    elif img_select == 'Starry Night':
        caption = 'Starry Night by Vincent Van Gogh'
        img_url = 'https://cdn.britannica.com/78/43678-050-F4DC8D93/Starry-Night-canvas-Vincent-van-Gogh-New-1889.jpg'
    elif img_select == 'The Persistence of Memory':
        caption = 'The Persistence of Memory by Salvador Dali'
        img_url = 'https://cdn.britannica.com/10/182610-050-77811599/The-Persistence-of-Memory-canvas-collection-Salvador-1931.jpg'

    # Caching this function so that on subsequent runs the app will quickly load the selected image
    @st.cache
    def get_img_array(img_url):
        response = requests.get(img_url)
        img_fetch = Image.open(BytesIO(response.content))
        img_array = np.array(img_fetch) # Converting to a Numpy array so we can change individual pixels of the image
        img = Image.fromarray(img_array)
        return img, img_array

    img, img_array = get_img_array(img_url)

    if treatment_select == 'None':

        st.subheader('Here\'s the image with no treatment')
        st.write('To have some fun choose one of the treatments from the sidebar 🎈')
        st.image(img, caption=caption, width=500)

    elif treatment_select == 'Gold frame':

        frame_size = st.slider('Change frame size', 10, 50)

        def framed_photo(df):
            img_array_framed = np.array(df)
            frame_color = [212,175,55]
            img_array_framed[0:frame_size] = frame_color
            img_array_framed[-frame_size:] = frame_color
            img_array_framed[:,0:frame_size] = frame_color
            img_array_framed[:,-frame_size:] = frame_color
            img_framed = Image.fromarray(img_array_framed)
            caption_framed = str(caption) + ' properly framed'
            st.image(img_framed, caption=caption_framed, width=500)

        framed_photo(img_array)

    elif treatment_select == 'Color tint':

        color_tint = st.selectbox('Choose color tint', ('','Red', 'Green', 'Blue'))

        def tint_image():
            if color_tint == 'Red':
                img_array_red = np.array(img_array).copy()
                img_array_red[:,:,0] = 185
                img_rosy = Image.fromarray(img_array_red)
                caption_red = str(caption) + ' wearing rose-colored glasses'
                st.image(img_rosy, caption=caption_red, width=500)
            elif color_tint == 'Green':
                img_array_green = np.array(img_array).copy()
                img_array_green[:,:,0] = 0
                img_underwater = Image.fromarray(img_array_green)
                caption_green = str(caption) + ' as seen from underwater'
                st.image(img_underwater, caption=caption_green, width=500)
            elif color_tint == 'Blue':
                img_array_blue = np.array(img_array).copy()
                img_array_blue[:,:,2] = 220
                img_cold = Image.fromarray(img_array_blue)
                caption_blue = str(caption) + ' on a cold winter\'s day'
                st.image(img_cold, caption=caption_blue, width=500)
            else:
                st.image(img, caption=caption, width=500)

        tint_image()


    elif treatment_select == 'Flip image':

        flip_direction = st.radio('Select flip direction', ('Normal', 'Horizontal', 'Vertical'))

        if flip_direction == 'Normal':
            st.image(img, caption=caption, width=500)
        elif flip_direction == 'Horizontal':
            img_array_flip = np.flip(img_array, 1)
            img_flip = Image.fromarray(img_array_flip)
            caption_flip = str(caption) + ' flipped horizontally'
            st.image(img_flip, caption=caption_flip, width=500)
        elif flip_direction == 'Vertical':
            img_array_flip = np.flip(img_array, 0)
            img_flip = Image.fromarray(img_array_flip)
            caption_flip = str(caption) + ' flipped vertically'
            st.image(img_flip, caption=caption_flip, width=500)

elif app_mode == 'Source code':
    'Add later'
