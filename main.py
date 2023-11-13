import os
from io import StringIO

import pandas as pd
import streamlit as st
if not os.path.exists("files"):
    os.mkdir("files")
st.header("发票上传")
st.divider()
st.subheader("发票信息填报")
# 选择发票类型
invoice_type = st.selectbox("发票类型", ["书籍、印刷类", "办公用品类", "服务费", "材料类","其他"])

if invoice_type == "其他":
    invoice_type = st.text_input("其他发票类型")

# 选择发票抬头
invoice_title = st.text_input("购货方信息", help="请输入供货方公司全称")
# 选择发票金额
invoice_amount = st.number_input("发票金额", help="请输入发票金额", min_value=0.0, max_value=100000000.0, value=0.0, step=0.01)
# 选择发票日期
invoice_date = st.date_input("发票日期", help="请选择发票上的开票日期")
# 上传发票
uploaded_file = st.file_uploader("上传发票", help="请上传发票", type="pdf")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    file_path = os.path.join("files", invoice_title+"_"+str(invoice_amount)+"_"+str(invoice_date)+".pdf")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("发票上传成功")
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)
st.subheader("发票信息确认")
# 显示发票类型
st.write(f"发票类型：{invoice_type}")
# 显示发票抬头
st.write(f"购货方信息：{invoice_title}")
# 显示发票金额
st.write(f"发票金额：{invoice_amount}")
# 显示发票日期
st.write(f"发票日期：{invoice_date}")
# 显示发票
st.link_button("查看发票", "https://www.baidu.com")
