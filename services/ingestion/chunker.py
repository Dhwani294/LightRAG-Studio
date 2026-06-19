from uuid import uuid4

from schemas.chunk import Chunk


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200,
    ) -> None:
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(
        self,
        text: str,
    ) -> list[Chunk]:

        if not text.strip():
            return []

        chunks: list[Chunk] = []

        start = 0
        index = 0

        while start < len(text):

            end = min(
                start + self.chunk_size,
                len(text),
            )

            chunk_text = text[start:end]

            chunks.append(
                Chunk(
                    chunk_id=str(uuid4()),
                    content=chunk_text,
                    chunk_index=index,
                    start_char=start,
                    end_char=end,
                    token_estimate=max(
                        1,
                        len(chunk_text) // 4,
                    ),
                )
            )

            start += (
                self.chunk_size
                - self.overlap
            )

            index += 1

        return chunks

    def count_chunks(
        self,
        text: str,
    ) -> int:
        return len(
            self.chunk(text)
        )

    def total_tokens(
        self,
        text: str,
    ) -> int:
        chunks = self.chunk(text)

        return sum(
            chunk.token_estimate
            for chunk in chunks
        )