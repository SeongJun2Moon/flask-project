from dataclasses import dataclass

@dataclass
class Dataset(object):

    context: str # 파일이 저장된 경로
    fname: str # 파일명
    train: object # train.csv 가 데이터프레임으로 전환된 객체
    text: object # test.csv 가 데이터프레임으로 전환된 객체
    id: str # 승객ID, 문제가 된다
    label: str # 승객ID에 따른 생존여부, 답이 된다.

    #__init__을 사용할 수 없을 때 getter와 setter를 오토형식으로 만든다

    @property
    def context(self): return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self): return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self): return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def text(self): return self._text

    @text.setter
    def text(self, text): self._text = text

    @property
    def id(self): return self._id

    @id.setter
    def id(self, id): self.id = id

    @property
    def label(self): return self._label

    @label.setter
    def label(self, label): self._label = label