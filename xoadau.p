def xoadau(tu):
  tu = re.sub('[êếềệễểeéèẹẽẻ]','e',tu)
  tu = re.sub('[áàạãảăắằẳẵặâấầậẫẩ]','a',tu)
  tu = re.sub('[đ]','d',tu)
  tu = re.sub('[íìịĩỉ]','i',tu)
  tu = re.sub('[óòỏọõơớờợỡởôốồộổỗ]','o',tu)
  tu = re.sub('[úùụủũưứừựữử]','u',tu)
  tu = re.sub('[ýỳỷỹỵ]','y',tu)
  return tu
