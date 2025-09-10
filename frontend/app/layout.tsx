// frontend/app/layout.tsx (RootLayout)
import "./globals.css";
import ThemeProvider from "../components/theme-provider";
import AppHeader from "../components/AppHeader";
import type { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-background text-foreground antialiased">
        <ThemeProvider>
          {/* Fill viewport and let <main> claim the rest */}
          <div className="min-h-screen flex flex-col">
            <AppHeader />
            <main className="flex-1 mx-auto max-w-7xl px-4 py-6 overflow-hidden">
              {children}
            </main>
          </div>
        </ThemeProvider>
      </body>
    </html>
  );
}