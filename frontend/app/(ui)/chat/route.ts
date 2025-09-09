// frontend/app/api/chat/route.ts
import { groq } from '@ai-sdk/groq';
import { convertToModelMessages, streamText, UIMessage } from 'ai';

// Ensure server (so we can read GROQ_API_KEY)
export const runtime = 'nodejs';
export const maxDuration = 30;

const MODEL = process.env.GROQ_MODEL || 'openai/gpt-oss-20b'; // fallback/change if needed

export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json();

  const result = streamText({
    model: groq(MODEL),
    // if you want to add a system prompt, do it here:
    // system: 'You are ARIA chat…',
    messages: convertToModelMessages(messages),
  });

  // Vercel AI SDK v5 data stream format (what DefaultChatTransport expects)
  return result.toDataStreamResponse();
}