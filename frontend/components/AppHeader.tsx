"use client";
import Link from "next/link";
import { useTheme } from "next-themes";
import { Sun, Moon } from "lucide-react";

export default function AppHeader({
  model = process.env.NEXT_PUBLIC_MODEL_NAME || "GPT-oss-20B",
}: { model?: string }) {
  const { theme, setTheme } = useTheme();
  const next = theme === "dark" ? "light" : "dark";

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/80 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="mx-auto max-w-7xl px-4 h-12 flex items-center gap-3">
        <Link href="/" className="font-semibold tracking-tight">ARIA Mission Control</Link>
        <span className="text-xs px-2 py-1 rounded-md border bg-muted text-muted-foreground">Model: {model}</span>
        <div className="ml-auto">
          <button
            onClick={() => setTheme(next)}
            className="h-8 w-8 inline-flex items-center justify-center rounded-md border bg-muted hover:opacity-90"
            aria-label="Toggle theme"
          >
            {theme === "dark" ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </button>
        </div>
      </div>
    </header>
  );
}