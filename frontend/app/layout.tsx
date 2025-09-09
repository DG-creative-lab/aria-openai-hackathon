import "./globals.css";
import ThemeProvider from "../components/theme-provider";
import AppHeader from "../components/AppHeader";
import type { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      {/* lock the shell to the viewport */}
      <body className="h-screen w-screen overflow-hidden bg-background text-foreground antialiased">
        <ThemeProvider>
          {/* App shell as a 2-row grid: header (auto) + content (1fr) */}
          <div className="grid h-screen grid-rows-[auto,1fr]">
            <AppHeader />
            {/* main fills remaining height; children manage their own overflow */}
            <main className="h-full overflow-hidden">
              <div className="mx-auto h-full max-w-7xl px-4 py-4">
                {children}
              </div>
            </main>
          </div>
        </ThemeProvider>
      </body>
    </html>
  );
}