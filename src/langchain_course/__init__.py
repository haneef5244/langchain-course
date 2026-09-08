from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_ollama import ChatOllama

load_dotenv()

def main() -> None:
    print("Hello from langchain-course!")

    information = """
Tun Dr. Mahathir bin Mohamad; dilahirkan pada 10 Julai 1925)[2][3][4] atau juga dikenali sebagai Tun M ialah seorang doktor dan ahli politik Malaysia yang berkhidmat sebagai Perdana Menteri Malaysia ke-4 (1981-2003) dan ke-7 (2018-2020). Perkhidmatan beliau sebanyak 2 kali dan 24 tahun menjadikan beliau sebagai Perdana Menteri yang paling lama berkhidmat dan yang pertama menyandang jawatan itu 2 kali. Dalam buku A Doctor in the House, Mahathir menyatakan tarikh lahir sebenarnya ialah 10 Julai 1925, tetapi bapanya mendaftarkan tarikh lahir dalam sijil kelahiran sebagai 20 Disember untuk memudahkan urusan pendaftaran persekolahan. Menggunakan nama timangannya sendiri, "Che Det" sebagai nama pena, beliau banyak menulis dengan artikel pertamanya disiarkan oleh akhbar The Straits Times Singapura pada 20 Julai 1947 bertajuk “Malay Women Make Their Own Freedom” (Wanita Melayu Mencipta Kebebasan Sendiri).[5] Semasa pentadbirannya dari 16 Julai 1981 sehingga 31 Oktober 2003, beliau berjaya membawa pembangunan melalui dasar-dasar dan perancangan yang diilhamkan daripada kejayaan negara-negara luar sehingga mengangkat Malaysia ke pentas dunia sebagai salah sebuah negara yang berdaya maju di Asia Tenggara.[6]

Mahathir dilahirkan pada 10 Julai 1925 di Kampung Seberang Perak, Alor Setar, Kedah. Beliau mendapat pendidikan awal di Sekolah Melayu Seberang Perak selama dua tahun sebelum memasuki sekolah Inggeris kerajaan yang kemudian bertukar nama kepada Kolej Sultan Abdul Hamid, di mana ayahnya adalah guru besar. Sebagai pelajar, Mahathir aktif berdebat dan dikenali dengan ntuk kemahiran bahasa Inggerisnya. Beliau dilantik sebagai editor majalah sekolah dan bermain untuk pasukan ragbi sekolah.

Semasa di kolej, Mahathir telah bertemu dengan Siti Hasmah Mohd Ali, juga seorang pelajar perubatan. Pada tahun 1956, mereka berkahwin dalam satu majlis di Jalan Imbi di Kuala Lumpur. Mereka mempunyai tujuh anak, iaitu Marina, Mirzan, Melinda, Mokhzani, Mukhriz, Maizura dan Mazhar.

Pada 1965, beliau dipilih sebagai Ahli Majlis Tertinggi UMNO dan pada PRU 1969, Mahathir bertanding PRU, tetapi ditewaskan oleh wakil PAS. Pada 1972, permohonan Mahathir untuk menyertai semula UMNO telah diterima dan beliau dilantik sebagai Senator pada 1973 serta ahli mahkamah universiti dan Majlis Universiti Malaya. Pada tahun berikutnya, beliau memenangi kerusi Kubang Pasu tanpa bertanding pada PRU tahun berkenaan sebelum dilantik sebagai Menteri Pendidikan dan menutup Klinik Maha di Alor Setar.

Pada tahun 1976, Mahathir dilantik sebagai Timbalan Perdana Menteri dan dua tahun kemudian, beliau mengambil alih jawatan Menteri Perdagangan dan Industri di mana beliau memimpin beberapa misi mempromosi pelaburan. Beliau pernah menjadi Perdana Menteri keempat Malaysia pada 16 Julai 1981, menyandang jawatan itu untuk tempoh yang paling lama dalam sejarah Malaysia dan Asia Tenggara, iaitu 22 tahun.

Antara projek-projek berprofil tinggi (juga digelar 'projek mega') yang dibangunkan pada zaman pentadbirannya termasuk Jambatan Pulau Pinang, Menara Berkembar Petronas, Lapangan Terbang Antarabangsa Kuala Lumpur (KLIA), Koridor Raya Multimedia (MSC), Pusat Pentadbiran Putrajaya dan Litar Antarabangsa Sepang. Mahathir juga menyatakan hasrat beliau untuk Malaysia melalui Wawasan 2020, iaitu visi negara untuk mencapai status ekonomi maju (developed nation) pada tahun 2020, bukan hanya dari segi pertumbuhan ekonomi tetapi juga dari segi pendidikan, kematangan masyarakat, dan tadbir urus. Malah beliau adalah satu-satunya pemimpin yang berjaya meletakkan Malaysia di peta dunia sebagai sebuah negara industri baru yang berpotensi dan berkembang maju. Namun beliau juga tidak terlepas dengan ujian dalam pentadbirannya apabila berdepan krisis kewangan Asia sekitar 1997-1998 namun berjaya melepasi tempoh mencabar itu. Pada tahun 1997, majalah Asiaweek telah menamakan Mahathir sebagai antara 50 individu yang paling berkuasa di Asia, di mana beliau menduduki tempat kedua dalam senarai yang dikeluarkan oleh majalah tersebut.[7]

Bersara pada Oktober 2003, Mahathir dianugerahkan Darjah Kebesaran Seri Maharaja Mangku Negara yang membawa gelaran Tun.[8] Beliau turut dinobatkan sebagai "Bapa Pemodenan Malaysia" kerana berjaya membangunkan Malaysia menjadi sebuah Negara industri baru yang disegani di kalangan negara-negara membangun. Tempoh 22 tahun sebagai Perdana Menteri menjadikan beliau sebagai pemimpin ketiga paling lama yang memegang jawatan tersebut di Asia Tenggara selepas Perdana Menteri Singapura pertama, Lee Kuan Yew dan diktator Suharto dari Indonesia. Beliau juga berkhidmat sebagai Canselor Universiti Teknologi Petronas (UTP) dari tahun 2004 hingga 2016.

Mahathir kekal sebagai tokoh politik aktif selepas bersara. Beliau menjadi pengkritik tinggi terhadap penggantinya yang dipilih Abdullah Ahmad Badawi pada tahun 2006 dan kemudiannya, Najib Razak pada 2015.[9] Anaknya Mukhriz Mahathir adalah Menteri Besar Kedah sehingga awal 2016. Pada 29 Februari 2016, Mahathir keluar dari UMNO memandangkan sokongan UMNO terhadap tindakan Perdana Menteri Najib Razak. Antara sebab lain ialah isu RM2.6bil dan 1Malaysia Development Berhad (1MDB).[10] Pada 9 September 2016, Pendaftar Pertubuhan (RoS) telah memberikan kelulusan terakhirnya untuk Parti Pribumi Bersatu Malaysia (PPBM) baru Mahathir, menjadikannya parti politik rasmi. Mahathir menjadi pengerusi parti itu.[11] Pada 8 Januari 2018, Mahathir diumumkan sebagai calon Pakatan Harapan untuk Perdana Menteri untuk pilihan raya 2018, dalam rancangan untuk mengampuni Anwar Ibrahim dan menyerahkan peranan kepadanya jika berjaya. Sehingga peletakan jawatannya pada 2020, beliau merupakan Perdana Menteri Malaysia yang tertua dan ketua negara atau kerajaan tertua di dunia.[12]

Pada 31 Ogos 2022, Mahathir disahkan positif Covid-19 dan dirawat di Institut Jantung Negara (IJN).[13][14][15] Selepas Pilihan Raya Umum ke-15, beliau mengumumkan akan menumpukan sepenuh perhatiannya untuk menulis mengenai sejarah Malaysia dan peristiwa semasa.[16] Pada 10 Julai 2025, Mahathir berusia 100 tahun.[17]
"""

    summary_template = """
Given the information {information} about a person, I want you to create:
1) A short summary
2) 2 interesting facts about the person
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatOllama(
        model="qwen",
        temperature=1
    )

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)
if __name__ == "__main__":
    main()