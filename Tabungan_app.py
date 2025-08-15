import streamlit as st

st.set_page_config(page_title="Simulasi Tabungan", page_icon="💰")

st.title("💰 Simulasi Tabungan")

# Pilih mode perhitungan
mode = st.radio("Pilih mode perhitungan:", ["Hitung Nominal per Hari/Bulan (Target)", "Hitung Total Terkumpul (Nominal per Hari)"])

# ================================
# MODE 1: Hitung Nominal per Hari/Bulan (sesuai target)
# ================================
if mode == "Hitung Nominal per Hari/Bulan (Target)":
    st.write("Hitung nominal per hari dan per bulan untuk mencapai target tabungan.")

    # 1. Pilihan waktu
    pilihan = st.selectbox("Pilih satuan waktu", ["Hari", "Bulan", "Tahun"])

    # 2. Lama menabung
    lama = st.number_input(f"Berapa lama menabung ({pilihan.lower()})", min_value=1, step=1)

    # 3. Target tabungan
    target = st.number_input("Masukkan target tabungan (Rp)", min_value=0.0, step=1000.0)

    # Hitung total hari
    if pilihan == "Hari":
        total_hari = lama
    elif pilihan == "Bulan":
        total_hari = lama * 30
    else:  # Tahun
        total_hari = lama * 365

    # Perhitungan
    if target > 0 and lama > 0:
        nominal_per_hari = target / total_hari

        st.subheader("📊 Hasil Perhitungan")
        st.write(f"Target tabungan: **Rp {target:,.2f}**")
        st.write(f"Lama menabung: **{total_hari} hari**")
        st.write(f"Nominal per hari: **Rp {nominal_per_hari:,.2f}**")

        # Tambahan nominal per bulan jika >= 1 bulan
        if total_hari >= 30:
            nominal_per_bulan = nominal_per_hari * 30
            st.write(f"Nominal per bulan: **Rp {nominal_per_bulan:,.2f}**")
    else:
        st.warning("Masukkan nilai target dan lama menabung yang valid.")

# ================================
# MODE 2: Hitung Total Terkumpul (Nominal per Hari)
# ================================
else:
    st.write("Hitung total tabungan jika menabung per hari sesuai keinginan.")

    # 1. Pilihan waktu
    pilihan = st.selectbox("Pilih satuan waktu", ["Hari", "Bulan", "Tahun"], key="mode2_waktu")

    # 2. Lama menabung
    lama = st.number_input(f"Berapa lama menabung ({pilihan.lower()})", min_value=1, step=1, key="mode2_lama")

    # 3. Nominal per hari
    nominal_harian = st.number_input("Masukkan nominal tabungan per hari (Rp)", min_value=0.0, step=1000.0)

    # Hitung total hari
    if pilihan == "Hari":
        total_hari = lama
    elif pilihan == "Bulan":
        total_hari = lama * 30
    else:  # Tahun
        total_hari = lama * 365

    # Perhitungan
    if nominal_harian > 0 and lama > 0:
        total_tabungan = nominal_harian * total_hari

        st.subheader("📊 Hasil Perhitungan")
        st.write(f"Nominal tabungan per hari: **Rp {nominal_harian:,.2f}**")
        st.write(f"Lama menabung: **{total_hari} hari**")
        st.write(f"Total tabungan terkumpul: **Rp {total_tabungan:,.2f}**")

        # Jika >= 1 bulan, tampilkan total per bulan
        if total_hari >= 30:
            total_per_bulan = nominal_harian * 30
            st.write(f"Tabungan per bulan: **Rp {total_per_bulan:,.2f}**")
    else:
        st.warning("Masukkan nominal per hari dan lama menabung yang valid.")
