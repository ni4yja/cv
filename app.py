import streamlit as st

st.set_page_config(
    page_title="Liubov Kuibida",
    page_icon="🪴",
)

st.title("Liubov Kuibida")
st.header("Kulturoznawczyni, programistka, mentorka. Łączę kulturę z technologią.")

skills, education, experience, volunteer = st.tabs(["Umiejętności", "Wykształcenie", "Doświadczenie", "Wolontariat"])

with skills:
    st.subheader("Narzędzia cyfrowe")
    st.write("MS Office (w tym Excel), Canva, Notion, WordPress, Google Analytics")
    st.subheader("Języki programowania")
    st.write("JavaScript, Python")
    st.subheader("Języki obce")
    st.write("ukraiński (ojczysty), polski (B2), angielski (C1)")
    st.subheader("Kompetencje miękkie")
    st.write("komunikatywność, samodzielność, dokładność, organizacja pracy")

with education:
    st.subheader("Kurs Podstawy programowania w Python")
    st.markdown(
        ":green-background[:green[PJATK]] :gray-background[:gray[Warszawa]] :violet-background[:violet[lipiec – sierpień 2025]]"
    )
    st.subheader("Język polski biznesowy w środowisku informatycznym")
    st.markdown(
        ":green-background[:green[Fukudenkai i EduMundi]] :gray-background[:gray[kurs online]] :violet-background[:violet[czerwiec – lipiec 2025]]"
    )
    st.subheader("Supporting the Creative Economy")
    st.markdown(
        ":green-background[:green[Cultural Associates Oxford]] :gray-background[:gray[kurs online]] :violet-background[:violet[kwiecień 2025]]"
    )
    st.subheader("Magister Kulturoznawstwa")
    st.markdown(
        ":green-background[:green[Uniwersytet Narodowy im. Iwana Franki]] :gray-background[:gray[Lwów]] :violet-background[:violet[2007 – 2012]]"
    )

with experience:
    st.subheader("Twórczyni treści i dziennikarka")
    st.markdown(
        ":green-background[:green[Happy Monday]] :gray-background[:gray[zdalnie]] :violet-background[:violet[listopad 2024 – lipiec 2025]]"
    )
    st.write("– Pisanie tekstów informacyjnych, edukacyjnych i promocyjnych")
    st.write("– Współpraca z zespołem redakcyjnym i eksperckim")
    st.write("– Publikacja artykułów w systemie WordPress")
    st.write("– Monitorowanie odbioru treści za pomocą Google Analytics")

    st.subheader("Frontend Developer (Vue.js)")
    st.markdown(
        ":green-background[:green[P2H]] :green-background[:green[UST]] :gray-background[:gray[zdalnie]] :violet-background[:violet[2018 – 2024]]"
    )
    st.write("– Rozwój wieloużytkownikowych portali")
    st.write("– pisanie i testowanie kodu (unit/integration testy)")
    st.write("– przeprowadzanie code review")
    st.subheader("Koordynatorka programu wystawienniczego")
    st.markdown(
        ":green-background[:green[Centrum Historii Miejskiej Europy Środkowo-Wschodniej]] :gray-background[:gray[Lwów]] :violet-background[:violet[2015]]"
    )
    st.write("– Opracowanie i archiwizacja materiałów tekstowych i wizualnych")
    st.write("– Współpraca przy tworzeniu cyfrowych baz danych i materiałów promocyjnych")
with volunteer:
    st.subheader("Mentorka w programach rozwojowych dla kobiet w IT")
    st.markdown(":green-background[:green[Vona Tech Community]] :green-background[:green[BE]] :violet-background[:violet[2022 – 2024]]")
    st.write("Wspierałam uczestniczki w rozwoju zawodowym, dzieliłam się doświadczeniem i pomagałam budować pewność siebie.")

