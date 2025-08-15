import streamlit as st

st.set_page_config(page_title="Simulasi Tabungan", page_icon="💰")

st.title("💰 Simulasi Tabungan")
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
