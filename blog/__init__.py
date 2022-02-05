class Base:
    header = "Это блок хедер"
    content = ""
    footer = "Это блок футер"


class ArticleList(Base):
    content = "Список артиклей"


class ArticleDetail(Base):
    content = "Детальная артикля"
