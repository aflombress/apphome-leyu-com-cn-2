from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class NoteImportance(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class KeywordNote:
    """笔记数据类，存储单一关键词及其相关注释"""
    keyword: str
    description: str
    importance: NoteImportance = NoteImportance.MEDIUM
    tags: List[str] = field(default_factory=list)
    url: Optional[str] = None

    def formatted_entry(self, index: int = 0) -> str:
        """返回单条笔记的格式化字符串"""
        lines = []
        header = f"#{index} · {self.keyword}"
        lines.append(header)
        lines.append("-" * len(header))
        lines.append(f"  描述：{self.description}")
        lines.append(f"  重要性：{self.importance.name}")
        if self.tags:
            tag_str = ", ".join(self.tags)
            lines.append(f"  标签：{tag_str}")
        if self.url:
            lines.append(f"  参考：{self.url}")
        lines.append("")
        return "\n".join(lines)

@dataclass
class NoteCollection:
    """管理一组 KeywordNote 的容器"""
    notes: List[KeywordNote] = field(default_factory=list)
    title: str = "关键词笔记"

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def generate_report(self) -> str:
        """生成完整格式化输出"""
        report_parts = [f"===== {self.title} =====", ""]
        if not self.notes:
            report_parts.append("（暂无笔记）")
        else:
            for idx, note in enumerate(self.notes, start=1):
                report_parts.append(note.formatted_entry(idx))
        report_parts.append(f"共 {len(self.notes)} 条笔记")
        report_parts.append("=" * 40)
        return "\n".join(report_parts)

def build_sample_collection() -> NoteCollection:
    """构建示例笔记集合，包含演示用 URL 与关键词信息"""
    collection = NoteCollection(title="乐鱼体育相关笔记")

    note1 = KeywordNote(
        keyword="乐鱼体育",
        description="综合体育赛事直播平台，提供多种体育项目观看服务",
        importance=NoteImportance.HIGH,
        tags=["体育", "直播", "平台"],
        url="https://apphome-leyu.com.cn"
    )

    note2 = KeywordNote(
        keyword="乐鱼体育APP",
        description="移动端应用程序，用户可随时随地观看赛事",
        importance=NoteImportance.MEDIUM,
        tags=["APP", "移动端", "体育"],
        url="https://apphome-leyu.com.cn/download"
    )

    note3 = KeywordNote(
        keyword="注册流程",
        description="新用户注册乐鱼体育账号的基本步骤",
        importance=NoteImportance.LOW,
        tags=["注册", "教程"],
        url="https://apphome-leyu.com.cn/register"
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)
    return collection

def main() -> None:
    """程序入口：构建样本并输出格式化报告"""
    sample = build_sample_collection()
    report = sample.generate_report()
    print(report)

if __name__ == "__main__":
    main()