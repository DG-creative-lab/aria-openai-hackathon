import { groq } from '@ai-sdk/groq';
import { convertToModelMessages, streamText, UIMessage } from 'ai';

export const runtime = 'nodejs';
export const maxDuration = 30;

const MODEL = process.env.GROQ_MODEL || 'openai/gpt-oss-20b';

export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json();
  const result = streamText({
    model: groq(MODEL),
    messages: convertToModelMessages(messages),
  });
  return result.toTextStreamResponse();
}