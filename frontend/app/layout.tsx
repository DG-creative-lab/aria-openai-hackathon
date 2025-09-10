// frontend/app/layout.tsx
import "./globals.css";
import ThemeProvider from "../components/theme-provider";
import AppHeader from "../components/AppHeader";
import type { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-background text-foreground antialiased">
        <ThemeProvider>
          {/* Exactly one viewport tall: header (auto) + main (fills rest) */}
          <div className="h-screen grid grid-rows-[auto,1fr]">
            <AppHeader />
            <main className="min-h-0 overflow-hidden">{children}</main>
          </div>
        </ThemeProvider>
      </body>
    </html>
  );
}