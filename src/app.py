import streamlit as st
from src.main import PinPasswordGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

col1, col2 = st.columns([1, 6])  
with col1:
    st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAaVBMVEX+2t7////+2eD92eD///7929z92t792uD8///34OT8293//f/+//383uP72eL76O7/+Pz36ur03eD//fr04uT45+n79fP/1t/88/P97+//9/z429312t3039///vr6//rz6ej97vL64+uB0j8OAAAE6ElEQVR4nO3a63biIBQF4IQkQC6M5go2UWvf/yEHYqfVBGvSaYt07e/HTFerLrYkwIEEEdGC3wwJ/UeQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADPLGdUu+CxL6bwzHDNct+S6/MeHrFSn1v7Tvq6Zty7Jt20awSEr9l6Sn+kWuW/kfzvec1P027EvVHQ6HQtP/1Z0qm+EXdOV4URLSV21XF8djcSmuVTOYHqaUum7n5+mAwnRfF8cx5zwMwzwP38Uq7bPM43znhENZFwUPTbIxI+dj1vOPhdr31NPJY7xAJRmaLja9Fd6kqoD4ObiOo0zf1sUH6cxVm6u98LIXqQk4lHrw/CigUdQNI0HiusHrERJVytyB9+h7tBVBkrlu8Gq6B/UEeLcHxzGnbrPEqyF1nOBI9bwk31neZnKcOl03fTE9i4t7g8xlN8ZdRX1L2DfLA+oLNVaVCehLQr3MzqpuecDRqfeoC00h0S4ZRt/lYZ7qhJ4MNzQhpKlXdaBWdELSLFnO4W6BHkpFuXgY/ecYp+va63I7hLKqXncThmYZrgRZxeFmARPtqpvwVd5EJFrO5XYIqxS3JeSxWWnrOiq251fpWv3PD03j5ZM1s2vUxDJVvWBsqFpln0nWXdn6+wp3rhKWtrbGSkSESINscmsnf2D+ifpbil0l7Lv5SBrrVcv4CrNrYWaT1UPR/BMdJqyPYT5tjqpMEZidRSzNV88nD5QwnRcVRZ5S+faqTNfH7Rck5M4SzgeSYseuS1wyrF712BL+eMAxIWvnWxd1epUwyaR49jdhtLMkFFer6iQjUeNvQqbmCVUk6cVmU9ITUnmc0NKHOuHl5rbuQyn8TjiZLELFgsu9pkS/0POE0+bkQ5BdlDo6ofD5Pizns0XcZJOEVelxwudiuqTRbcmS94Q0I2Tv6Xw4tn9v2SjNm/6qIBfPx69I6Ghjp6/nnRiqvW4NPS9MKRHl8u3i2wldVE/nhGp2H3Ieq6Y/n/ZSStnzcTbcfiqhm4BBb6kPdT24TXtGpNlfMfvh815em1B/gquEWRPOC1z9m7prK1FVTdkdithWAvNxl2PCls783nyLrhKSYWst4U1Fd96nse1i8HAnLCyTyvbl3x+dnR2zNvzMXls63S/UqwRmSfj0h5BxWeTuGIAO2/UBw5MIJglNCWLrQ9cJdRGhO3H1PozuwiDwI6FevZBqfSeqPzKhfiQ0aMvDNfMBj/Nqfrr2cULHhLqxsW0PGMblEPmVkIh8eUKz4rGdAT92QrJisIkLlTLLOf5DJ6SMbZZep3HRNURK3xISMqiiuLHqusQ5z28cjj50wvGZqN2tc7TLfHoFnUYksNVBD52Qjoe0m3snpWb92pnVmn8JXx9bT7d3hhue7yp6q8EPnXDsQhFJMa+Gr+SnwdTESWJrsT0hf4yE71KV36g0ON+eBBPi5lbErYTisRIysdnm45B5mW186Pvp5c+HzxvYEurB+emx+pBKGQ3njJNn9XepIPJ+Qn7tAa9SjVEm2l1X14dRcdjuTmnav9VKN9/ox31oBhGTIemFSFttk6ZRFEkZEHnnyabxEG4zdXqRj5Xw3XSP4lPvWvPWH4eEi96FhE59WcJvbSUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADA//gLyBhNnZo547oAAAAASUVORK5CYII=", width=100 )

with col2:
    st.title(":maple_leaf: Password Generator")
    
option = st.radio("Pick one",('Pin password', 'Random password', 'Memorable password')
        )
if option == 'Pin password':
    length = st.slider("Chosse your password length: ", 4, 32)
    generator = PinPasswordGenerator(length)

elif option == 'Random password':
    length = st.slider("Chosse your password length: ", 4, 32)
    include_numbers = st.toggle("Include number")
    include_symbols = st.toggle("Include symbol")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

elif option == 'Memorable password':
    num_of_words = st.slider("Chosse your number of words: ", 2, 32)
    seteperator = st.text_input("Seperator", '-')
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(num_of_words, seteperator, capitalization)


password = generator.generate()
message = st.write(fr"Your password:``` {password} ``` ")
