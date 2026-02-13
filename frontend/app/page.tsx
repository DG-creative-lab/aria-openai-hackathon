// frontend/app/page.tsx
import PlanPanel from "../components/PlanPanel";
import Gauges from "../components/Gauges";
import Timeline from "../components/Timeline";
import ChatPanel from "./(ui)/chat/ChatPanel";
import ScenarioControls from "../components/ScenarioControls";

export default function Page() {
  const base = process.env.NEXT_PUBLIC_API_BASE || "";

  return (
    <div className="h-full min-h-0 mx-auto max-w-7xl p-4 flex flex-col">
      {/* header row of the page (doesn't grow) */}
      <div className="mb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2 shrink-0 min-w-0">
        <div className="text-sm text-muted-foreground">ARIA Mission Control</div>
        <ScenarioControls />
      </div>

      {/* the big grid consumes remaining height */}
      <div className="grid flex-1 min-h-0 grid-cols-1 gap-4 lg:grid-cols-12">
        {/* LEFT */}
        <aside className="lg:col-span-4 min-h-0">
          <div className="panel h-full flex flex-col">
            <div className="panel-header shrink-0">Mission Chat</div>
            <div className="panel-body flex-1 min-h-0 overflow-hidden">
              <ChatPanel />
            </div>
          </div>
        </aside>

        {/* RIGHT */}
        <section className="lg:col-span-8 grid min-h-0 overflow-hidden grid-rows-[minmax(360px,3fr),minmax(240px,2fr)] gap-4">
          <div className="grid min-h-0 overflow-hidden grid-cols-1 gap-4 xl:grid-cols-[minmax(0,2fr)_minmax(300px,1fr)]">
            <div className="min-h-0">
              <div className="panel h-full flex flex-col">
                <div className="panel-header shrink-0">Flight Gauges</div>
                <div className="panel-body flex-1 min-h-0 overflow-hidden">
                  <Gauges backendBase={base} />
                </div>
              </div>
            </div>
            <div className="min-h-0">
              <div className="panel h-full flex flex-col">
                <div className="panel-header shrink-0">ARIA Plan</div>
                <div className="panel-body flex-1 min-h-0 overflow-hidden">
                  <PlanPanel backendBase={base} />
                </div>
              </div>
            </div>
          </div>

          <div className="panel h-full flex flex-col">
            <div className="panel-header shrink-0">Timeline</div>
            <div className="panel-body flex-1 min-h-0 overflow-hidden p-0">
              <Timeline backendBase={base} />
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
